#!/usr/bin/env python3
import argparse
import re
from rosmsg_idl_converter import utils


def convert_idl_to_msg(idl_file, output_dir):
    content = utils.extract_content_from_file(idl_file)

    struct_pattern = re.compile(r'struct\s+(\w+)\s*\{([^}]*)\}', re.MULTILINE)
    field_pattern = re.compile(r'(\w+)\s+(\w+);')

    for struct_name, struct_body in struct_pattern.findall(content):
        field_matches = field_pattern.findall(struct_body)
        msg_content = ""
        for field_type, field_name in field_matches:
            msg_type = utils.TYPE_MAPPING_IDL2MSG[field_type]
            msg_content += f"{msg_type} {field_name}\n"
        msg_content = msg_content[:-1]

        msg_file_path = f"{utils.rstrip_path(output_dir)}/{struct_name}.msg"
        with open(msg_file_path, 'w') as msg_file:
            msg_file.write(msg_content)

        print(f"Converted {struct_name} to ROS msg: {msg_file_path}")


def main():
    parser = argparse.ArgumentParser(description="Convert IDL files to ROS msg files.")
    parser.add_argument("idl_file", help="Path to the IDL file to be converted.")
    parser.add_argument("output_dir", help="Output directory to store the generated ROS msg files.")
    args = parser.parse_args()
    convert_idl_to_msg(args.idl_file, args.output_dir)


if __name__ == "__main__":
    main()
