import codecs
import os
import re

from setuptools import setup, find_packages

PACKAGES = find_packages(where="src")
META_PATH = os.path.join("src", "fotomanager", "__init__.py")
README = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "README.md")
LICENSE = os.path.join(os.path.dirname(
    os.path.abspath(os.path.dirname(__file__))), "LICENSE")


setup(
        name="fotomanager",
        version="0.2.1",
        url='https://github.com/ashishrv/phototools.git',
        description="Photography Workflow Tools",
        long_description=open(README).read(),
        long_description_content_type="text/markdown",
        author="Ashish Vidyarthi",
        author_email="ashish.vid@gmail.com",
        license = open(LICENSE).read(),
        packages=["fotomanager"],
        package_dir={"": "src"},
        install_requires=["fire"],
    entry_points={"console_scripts": [
        "foto-copyraw = fotomanager.bin.copyraw:main", "foto-manager = fotomanager.bin.manager:main"]},
)
