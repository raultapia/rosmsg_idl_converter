from setuptools import setup, find_packages

setup(
    name='rosmsg_idl_converter',
    author="Raul Tapia",
    author_email="raultapia@us.es",
    license="GPLv3",
    version='1.0.0',
    setup_requires=['setuptools'],
    install_requires=['argparse'],
    packages=find_packages(include=['rosmsg_idl_converter']),
    entry_points={'console_scripts': ['idl2msg=rosmsg_idl_converter.idl2msg:main', 'msg2idl=rosmsg_idl_converter.msg2idl:main']}
)
