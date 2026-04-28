"""Auto-generate op_specs from ONNX schema.

Usage:
  python schema_gen.py                    # generate for default opset
  python schema_gen.py --opsets 11 14 16  # specific opsets
  python schema_gen.py --output json      # json or python
  python schema_gen.py --save specs.json
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from dataclasses import dataclass, asdict

try:
    from onnx import defs
except ImportError:
    print("Error: onnx package not installed")
    sys.exit(1)


@dataclass
class AttrSpec:
    """Attribute specification extracted from ONNX schema."""
    attr_type: str  # "INT", "INTS", "FLOAT", "FLOATS", "STRING", "STRINGS"
    required: bool
    default_value: str | int | float | None
    description: str


@dataclass
class VariadicSpec:
    """Variadic input specification."""
    min_arity: int
    is_homogeneous: bool


@dataclass
class OpProfile:
    """Complete operator profile extracted from ONNX schema."""
    name: str
    opset: int
    # inputs: list of (name, type_param, is_optional)
    inputs: list[tuple[str, str, bool]]
    # outputs: list of (name, type_param, is_optional)
    outputs: list[tuple[str, str, bool]]
    # attributes: name -> AttrSpec
    attributes: dict[str, AttrSpec]
    # type_constraints: type_param -> [allowed dtypes]
    type_constraints: dict[str, list[str]]
    # variadic_inputs: input_name -> VariadicSpec (only for variadic inputs)
    variadic_inputs: dict[str, VariadicSpec]
    # tied_dtypes: input_name -> tied_to_input_name (inputs with same type_param)
    tied_dtypes: dict[str, str]

    @property
    def input_names(self) -> list[str]:
        """Just the names."""
        return [name for name, _, _ in self.inputs]

    @property
    def required_inputs(self) -> list[str]:
        """Input names that are required (not optional)."""
        return [name for name, _, is_opt in self.inputs if not is_opt]

    @property
    def optional_inputs(self) -> list[str]:
        """Input names that are optional."""
        return [name for name, _, is_opt in self.inputs if is_opt]


def extract_dtype(type_str: str) -> str:
    """Convert 'tensor(float)' to 'float', etc."""
    if type_str.startswith("tensor("):
        return type_str.replace("tensor(", "").replace(")", "")
    return type_str


def _attr_type_str(attr_type) -> str:
    """Convert AttrType enum to string like 'INT', 'INTS', 'FLOAT', etc."""
    type_name = str(attr_type).split(".")[-1]
    return type_name


def profile_operator(op_name: str, opset: int = 11) -> OpProfile | None:
    """Extract complete operator profile from ONNX schema."""
    try:
        schema = defs.get_schema(op_name, opset)
    except Exception:
        return None

    # Extract inputs with type params and optional flags
    inputs = [
        (inp.name, inp.type_str, inp.option.name == "Optional")
        for inp in schema.inputs
    ]

    # Extract outputs with type params and optional flags
    outputs = [
        (out.name, out.type_str, out.option.name == "Optional")
        for out in schema.outputs
    ]

    # Extract attribute specs
    attributes = {}
    for attr_name, attr in schema.attributes.items():
        attr_type_str = _attr_type_str(attr.type)

        # Extract default value if present
        default_val = None
        if attr.default_value:
            try:
                # Default values are protobuf messages, try to extract scalar
                if hasattr(attr.default_value, 'i'):
                    default_val = attr.default_value.i
                elif hasattr(attr.default_value, 'f'):
                    default_val = attr.default_value.f
                elif hasattr(attr.default_value, 's'):
                    default_val = attr.default_value.s.decode('utf-8') if isinstance(attr.default_value.s, bytes) else attr.default_value.s
            except:
                default_val = None

        attributes[attr_name] = AttrSpec(
            attr_type=attr_type_str,
            required=attr.required,
            default_value=default_val,
            description=attr.description or "",
        )

    # Extract type constraints
    type_constraints = {}
    for tc in schema.type_constraints:
        dtypes = [extract_dtype(t) for t in tc.allowed_type_strs]
        type_constraints[tc.type_param_str] = sorted(set(dtypes))

    # Extract variadic input specs
    variadic_inputs = {}
    for inp in schema.inputs:
        is_variadic = inp.option.name == "Variadic"
        if is_variadic:
            variadic_inputs[inp.name] = VariadicSpec(
                min_arity=inp.min_arity,
                is_homogeneous=inp.is_homogeneous,
            )

    # Extract tied dtypes (inputs with same type_param must have same dtype)
    tied_dtypes = {}
    type_to_inputs = defaultdict(list)
    for name, type_param, _ in inputs:
        type_to_inputs[type_param].append(name)

    for type_param, names in type_to_inputs.items():
        if len(names) > 1:
            first = names[0]
            for other in names[1:]:
                tied_dtypes[other] = first

    return OpProfile(
        name=op_name,
        opset=opset,
        inputs=inputs,
        outputs=outputs,
        attributes=attributes,
        type_constraints=type_constraints,
        variadic_inputs=variadic_inputs,
        tied_dtypes=tied_dtypes,
    )


def generate_profiles(opsets: list[int]) -> dict[tuple[str, int], OpProfile]:
    """Generate profiles for all operators across opsets."""
    profiles = {}
    all_schemas = defs.get_all_schemas()

    # Extract op names from schema list
    op_names = sorted(set(schema.name for schema in all_schemas))

    for op_name in op_names:
        for opset in opsets:
            profile = profile_operator(op_name, opset)
            if profile:
                profiles[(op_name, opset)] = profile

    return profiles


def map_onnx_dtype_to_test_dtype(onnx_dtype: str) -> str | None:
    """Map ONNX dtype to our test dtype names."""
    mapping = {
        "float": "float32",
        "double": "float64",
        "float16": "float16",
        "int8": "int8",
        "int16": "int16",
        "int32": "int32",
        "int64": "int64",
        "uint8": "uint8",
        "uint16": "uint16",
        "uint32": "uint32",
        "uint64": "uint64",
        "bool": "bool",
    }
    return mapping.get(onnx_dtype)


def render_profiles_as_json(profiles: dict[tuple[str, int], OpProfile]) -> str:
    """Render profiles as JSON for inspection and code generation."""
    data = {}
    for (op_name, opset), profile in sorted(profiles.items()):
        key = f"{op_name}_opset{opset}"

        # Convert inputs/outputs tuples to dicts
        inputs_info = [
            {"name": n, "type_param": t, "is_optional": is_opt}
            for n, t, is_opt in profile.inputs
        ]
        outputs_info = [
            {"name": n, "type_param": t, "is_optional": is_opt}
            for n, t, is_opt in profile.outputs
        ]

        # Convert AttrSpec to dict
        attrs_dict = {}
        for attr_name, attr_spec in profile.attributes.items():
            attrs_dict[attr_name] = {
                "type": attr_spec.attr_type,
                "required": attr_spec.required,
                "default": attr_spec.default_value,
                "description": attr_spec.description,
            }

        # Convert VariadicSpec to dict
        variadic_dict = {}
        for inp_name, var_spec in profile.variadic_inputs.items():
            variadic_dict[inp_name] = {
                "min_arity": var_spec.min_arity,
                "is_homogeneous": var_spec.is_homogeneous,
            }

        data[key] = {
            "name": profile.name,
            "opset": profile.opset,
            "inputs": inputs_info,
            "outputs": outputs_info,
            "attributes": attrs_dict,
            "type_constraints": profile.type_constraints,
            "variadic_inputs": variadic_dict,
            "tied_dtypes": profile.tied_dtypes,
        }

    return json.dumps(data, indent=2)


def render_profiles_as_python(profiles: dict[tuple[str, int], OpProfile]) -> str:
    """Render profiles as Python code template (for future code generation)."""
    lines = [
        '"""Auto-generated op_specs from ONNX schema.',
        '',
        'This is a template showing how to use the extracted profiles.',
        'Run schema_gen.py with --output json to get the full data.',
        '"""',
        'from __future__ import annotations',
        '',
        '# To generate actual op_specs, extract required_inputs, optional_inputs,',
        '# and attribute types from the JSON profiles and use templates like:',
        '#',
        '# For unary ops with no attrs:',
        '#   unary_op("OpName", dtypes=extracted_dtypes)',
        '#',
        '# For binary broadcast ops:',
        '#   binary_broadcast_op("OpName", dtypes=extracted_dtypes)',
        '#',
        '# For ops with optional inputs or special attrs:',
        '#   OpSpec(',
        '#       name="OpName",',
        '#       inputs=(...),  # with tied_dtype_to set from profile.tied_dtypes',
        '#       attrs={...},   # built from profile.attributes',
        '#   )',
        '',
        '# See op_profiles_discovered.json for complete extracted data',
    ]
    return "\n".join(lines)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Auto-generate op_specs from ONNX schema"
    )
    parser.add_argument(
        "--opsets", type=int, nargs="+", default=[11, 13, 14, 16],
        help="Opset versions to profile"
    )
    parser.add_argument(
        "--output", choices=["json", "python"], default="json",
        help="Output format"
    )
    parser.add_argument(
        "--save", help="Save output to file"
    )

    args = parser.parse_args()

    print(f"Profiling {len(defs.get_all_schemas())} operators across opsets {args.opsets}...")

    profiles = generate_profiles(args.opsets)
    print(f"Generated {len(profiles)} operator profiles\n")

    if args.output == "json":
        output = render_profiles_as_json(profiles)
        print("=== JSON Output (sample) ===")
    else:
        output = render_profiles_as_python(profiles)
        print("=== Python Output (sample) ===")

    # Print first 2000 chars
    print(output[:2000])
    if len(output) > 2000:
        print(f"\n... ({len(output) - 2000} more characters)\n")

    if args.save:
        with open(args.save, "w") as f:
            f.write(output)
        print(f"\nSaved to {args.save}")
    else:
        print("\nUse --save FILE to save output")


if __name__ == "__main__":
    main()
