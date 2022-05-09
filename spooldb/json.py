"""A very untested json encoder and decoder"""

import json
from .spooldb import SpoolDB

class SpoolDBJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, "__dict__"):
            return o.__dict__

class SpoolDBJSONDecoder(json.JSONDecoder):
    def default(self, o):
        if isinstance(o, dict):
            db = SpoolDB(None)
            db.__dict__ = o

def toJSON(o: SpoolDB):
    return json.dumps(o, cls=SpoolDBJSONEncoder)