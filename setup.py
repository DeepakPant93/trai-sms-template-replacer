from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'This package to replace content in the TRAI SMS template'


# Setting up
setup(
    name="traisms",
    version=VERSION,
    author="Deepak Pant",
    author_email="<deepak.93p@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    python_requires = '>=3.7',
    include_package_data = True,
    keywords=['python', 'trai', 'sms', 'replace'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ]
)
