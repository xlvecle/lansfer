import codecs
from setuptools import setup, find_packages

setup(
    name = "lansfer",
    version = "0.1.2",
    packages = ['lansfer'],
    package_data = {
    },
    author = "xlvecle",
    author_email = "xingke0@gmail",
    description = "A simple tool for transfer file in LAN",
    license = '''            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

    ''',
    entry_points="""
    [console_scripts]
    rf = lansfer.rf:main
    sf = lansfer.sf:main
    """,
    url='xlvecle.github.io/lansfer'
)
