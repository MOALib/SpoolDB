"""
Abstract backend for SpoolDB
"""

from abc import ABC, abstractmethod

class SpoolDBAbstractBackend(ABC, object):
    """Do not use, it is broken"""
    def __init__(self):
        raise ValueError("Broken rn")

    @abstractmethod
    def load(self, fileobj):
        """
        Load data from a file-like object.

        Return a value please
        """
        pass

    @abstractmethod
    def dump(self, data, fileobj):
        """
        Dump data to a file-like object.
        """
        pass