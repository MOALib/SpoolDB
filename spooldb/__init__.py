"""
Everything needed together for SpoolDB

With a little test program built in.

It contains the database and some functions
"""

from .spooldb import SpoolDB
from .dbfunc import open, openshelve
from .abstractbackend import SpoolDBAbstractBackend
from .json import SpoolDBJSONEncoder, SpoolDBJSONDecoder

NAME="SpoolDB"

VERSION_INFO = (0, 2, 0)
VERSION = '.'.join(map(str, VERSION_INFO))
__version__ = VERSION

__author__ = "MXPSQL"

__description__ = "Python persistent dictionary (a key value store)"

__source_url__ = "https://github.com/MOALib/SpoolDB"

# Example program embedded
if __name__ == "__main__":
    with open('test.db', flag='c', format='json') as db:
        db["yes"] = "yes"
        db["high heel"] = "spool pumps"
        db["i"] = {
            "map": True,
            "list": [1, 2, 3],
            "tdb": {
                'ls': "true",
                "dir": True,
                "pax": True,
                "node": 'yes'
            }
        }
        db["lisp"] = ["common lisp", "scheme", "clojure"]

        for i in range(0, 5):
            db[i] = i