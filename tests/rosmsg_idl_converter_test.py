import os
from rosmsg_idl_converter import idl2msg
from rosmsg_idl_converter import msg2idl

TEST_FOLDER = os.path.dirname(os.path.realpath(__file__)) + '/'


def test_idl2msg():
    idl2msg.convert_idl_to_msg(TEST_FOLDER + 'example_idl.idl', TEST_FOLDER)
    with open(TEST_FOLDER + 'Data1.msg', 'r') as file:
        text = '\n'.join([x.lstrip() for x in file.read().split('\n')])
        expected = """string name\nint32 age\nfloat32 weight"""
        assert text == expected
    with open(TEST_FOLDER + 'Data2.msg', 'r') as file:
        text = '\n'.join([x.lstrip() for x in file.read().split('\n')])
        expected = """string name\nfloat64 age"""
        assert text == expected
    os.remove(TEST_FOLDER + 'Data1.msg')
    os.remove(TEST_FOLDER + 'Data2.msg')


def test_msg2idl():
    msg2idl.convert_msg_to_idl(TEST_FOLDER + 'ExampleMessage.msg', TEST_FOLDER)
    with open(TEST_FOLDER + 'ExampleMessage.idl', 'r') as file:
        text = '\n'.join([x.lstrip() for x in file.read().split('\n')])
        expected = """module Generated {{\nstruct ExampleMessage {\nstring name;\nlong age;\nfloat weight;\n}};\n}};"""
        assert text == expected
    os.remove(TEST_FOLDER + 'ExampleMessage.idl')


if __name__ == "__main__":
    test_idl2msg()
    test_msg2idl()
