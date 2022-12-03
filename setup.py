from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'A Project which allows you to use colors in the terminal!'
LONG_DESCRIPTION = 'A Project which allows you to use colors in the terminal!'

# Setting up
setup(
    name="color4py",
    version=VERSION,
    author="hayoto",
    author_email="<hayoto.dev@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["colorama", "fade"],
    keywords=['coloring', 'colors', 'fading', 'fade'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
