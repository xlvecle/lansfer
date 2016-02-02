import codecs
from setuptools import setup, find_packages

setup(
    name = "lanrfsf",
    version = "0.1",
    packages = ['lanrfsf'],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        # '': ['*.txt', '*.rst'],
        # # And include any *.msg files found in the 'hello' package, too:
        # 'hello': ['*.msg'],
    },
    # metadata for upload to PyPI
    author = "xlvecle",
    author_email = "xingke0@gmail",
    description = "A simple tool for transfer file in LAN",
    license = "PSF",
    entry_points="""
    [console_scripts]
    rf = lanrfsf.rf:main
    sf = lanrfsf.sf:main
    """,
    url='https://github.com/404'  # project home page, if any
    # could also include long_description, download_url, classifiers, etc.
)
