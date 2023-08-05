#!/usr/bin/env python3
def extract_content_from_file(input_file):
    ret = ""
    with open(input_file, 'r') as infile:
        for line in infile:
            line_without_comments = line.split('#')[0].strip()
            if line_without_comments:
                ret += line_without_comments + '\n'
    return ret[:-1]


def rstrip_path(s):
    if s[-1] == '/':
        return s[:-1]
    else:
        return s


TYPE_MAPPING_MSG2IDL = {
    'bool': 'boolean',
    'byte': 'octet',
    'char': 'uint8',
    'int8': 'int8',
    'uint8': 'uint8',
    'int16': 'int16',
    'uint16': 'uint16',
    'int32': 'int32',
    'uint32': 'uint32',
    'int64': 'int64',
    'uint64': 'uint64',
    'float32': 'float',
    'float64': 'double',
    'string': 'string',
    'wstring': 'wstring',
}

TYPE_MAPPING_MSG2IDL = {
    "bool": "boolean",
    "byte": "char",
    "float32": "float",
    "float64": "double",
    "int16": "short",
    "int32": "long",
    "int64": "long long",
    "int8": "octet",
    "string": "string",
    "uint16": "unsigned short",
    "uint32": "unsigned long",
    "uint64": "unsigned long long",
    "uint8": "unsigned octet",
    'wstring': 'wstring',
}

TYPE_MAPPING_IDL2MSG = {v: k for k, v in TYPE_MAPPING_MSG2IDL.items()}
