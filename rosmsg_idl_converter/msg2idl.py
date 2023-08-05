#!/usr/bin/env python3
import argparse
import re
import os
from rosmsg_idl_converter import utils


def convert_msg_to_idl(msg_file, output_dir):
    content = utils.extract_content_from_file(msg_file)
    msg_name = os.path.basename(msg_file).split(".")[0]

    field_pattern = r"(\S+)\s+(\S+)"
    field_lines = re.findall(field_pattern, content)

    idl_content = "module Generated {{\n"
    idl_content += f"    struct {msg_name} {{\n"

    for field_type, field_name in field_lines:
        idl_type = utils.TYPE_MAPPING_MSG2IDL.get(field_type, field_type)
        idl_content += f"        {idl_type} {field_name};\n"

    idl_content += "    }};\n"
    idl_content += "}};"

    output_file_path = os.path.join(utils.rstrip_path(output_dir), f"{msg_name}.idl")
    with open(output_file_path, 'w') as idl_file:
        idl_file.write(idl_content)

    print(f"Converted {msg_name} to IDL: {output_file_path}")


def main():
    parser = argparse.ArgumentParser(description="Convert ROS msg files to IDL.")
    parser.add_argument("msg_file", help="Path to the ROS msg file to be converted.")
    parser.add_argument("output_dir", help="Output directory to store the generated IDL files.")
    args = parser.parse_args()
    convert_msg_to_idl(args.msg_file, args.output_dir)


if __name__ == "__main__":
    main()
