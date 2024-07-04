from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.13'
DESCRIPTION = 'BytePost is a versatile Python module for sending HTTP requests'
LONG_DESCRIPTION = 'BytePost is a versatile Python module for sending HTTP requests using aiohttp, requests, and tls_client. It supports multiple HTTP methods and saves responses in a pretty-printed JSON format.'

setup(
    name="bytepost",
    version=VERSION,
    author="BytePulze",
    author_email="<eth2complicated@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'aiohttp', 'tls_client', 'colorama', 'asyncio'],
    keywords=['python', 'request', 'http', 'http request'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
