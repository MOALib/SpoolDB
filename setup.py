import setuptools as st
import spooldb

__long_description__ = ""
with open("README.md", "r") as fh:
    __long_description__ = fh.read()

__project__ = "SpoolDB"
__version__ = spooldb.VERSION
__description__ = spooldb.__description__
__packages__ = ["spooldb"]
__author__ = spooldb.__author__
__author__email__ = "2000onetechguy@gmail.com"
__keywords__ = ["Dict", "Persistent", "Database", "JSON", "CSV", "Shelf", "Pickle"]
__source__ = spooldb.__source_url__
__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.6",
]

st.setup(
    name=__project__,
    version=__version__,
    description=__description__,
    packages=__packages__,
    author=__author__,
    author_email=__author__email__,
    url=__source__,
    keywords=__keywords__,
    classifiers=__classifiers__,
)