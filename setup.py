from setuptools import setup, find_packages

import rpcviaredis

setup(
    name="rpcviaredis",
    PY_MODULES=['rpcviaredis']
    version=open("VERSION").read(),
    packages=find_packages(),
    author="Oscar LASM",
    author_email="lasm.landry@gmail.com",
    KEYWORDS=['Redis','RPC']
    description="Build RPC pattern via redis connection",
    long_description=open('README.md').read(),
    install_requires=['redis'],
    extras_require = {'msgpack': 'msgpack-python'},
    include_package_data=True,
    url='https://github.com/moas/rpcviaredis',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Object Brokering',
	'Topic :: System :: Distributed Computing'
    ],
    license="GNU V2.0",
)
