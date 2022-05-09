#!/bin/env python3
# 
# SpoolDB, a python dict, with multiple save fmt
# A better version of https://code.activestate.com/recipes/576642/
# 🥿 💅🏻👠 🩰 👢
# 
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓███████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓███████████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█████▓▒▓█████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██████▒▒▒▒▓███▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▒░░░▒█████▓▒▒▒▒▒████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░████▓▒░░▒▓████▒░░▒▒▒▓████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░▓██████▓░░░░▓███▒░░░░▒▒▓████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░▓█████████▒░░▒█▓██▓▒░░░░▒▒▓███▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░▒███████████▓░▒█▓▒▓███▒░░░▒▒▒▓███▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░███▓▒▒▓▓▓████▓▓██▓░▒███▓░░░░▒▒▒███▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░▒███▓▒▒▒▒▒▓████▓░▒▒░░▒███▓░░░░▒▒▒▓███▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░▒███▒▒▒▒▒▒▒▓████▒░░░▒▒▒███▓░░░▒▒▒▒▒████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░███▒▒▒░░░▒▒▓████▒░░░▒▒▒███░░░▒▒▒▒▒▓▓███▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░▓██▒▒▒░░░░░▓████▓░░░░▒▒▓██▓▒▒▒▒▒▓▓▓██████▓░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░▒██▒▒▒░░░░░▓█████▓░░░░▒▒▓██████████████████▒░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░▓█▓▒▒░░░░░▓██████▒░░░░▒▒███████████████████▓░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░▓██▒▒▒░░░░▓███████▒░░░░░▒████████████████████▒░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░▒██▓▒▒░░░░▒████████░░░░░░░▒▓██████████████████▒░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░▒▓█▓░▒░░░░░▓███████▒░░░░░░░░░▒▒▓▓██████████████▒░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░▒▓█▓░▒░░░░░▒████████░░░░░░░░░░░░░░▒▒▒▓▓█████████░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░▒▒█▓░▒▒░░░░░▒███████▓░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓▒░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▒▒▒░░░░░░▒███████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█▓▒▒░░░░░░░░▒█████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░▒▓██▒▒▒░░░░▒▒▒▒▒▓████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░▒▓███▓▒▒▒▒▒▒▒▒▒▒▓▓███▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░▓█████▓▓▓▓▓▓▓████████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░▒████████████████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░▒███████████████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓██████████████████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█████████████████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓███████████████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓██████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

"""
Database module
"""

import pickle, json, csv, os, shutil, random, datetime, inspect, sys
from .abstractbackend import SpoolDBAbstractBackend

class SpoolDB(dict, object):
    ''' Persistent database with the dictionary API as it inherits from the python dict.

    Output file fmt available is pickle and json.
    '''

    def __init__(self, filename=None, data={}, flag='c', mode=None, fmt='pickle', pickleopts=None, *args, **kwds):
        """ The spooldb constructor.
        """

        random.seed(f"{str(os.urandom(32))}{str(datetime.datetime.now())}")

        self.flag = flag                    # r=readonly, c=create, or n=new
        self.mode = mode                    # None or an octal triple like 0644
        self.fmt = fmt                # 'csv', 'json', 'pickle' or any SpoolDBAbstractBackend subclass
        self.filename = filename
        self.__accesskey = random.randint(0, sys.maxsize) # used for some private methods or functionalities in public methods
        self.pickleopts = pickleopts or {
            'protocol': 2,
        }
            

        dict.__init__(self, data)
        if filename != None and flag != 'n' and os.access(filename, os.R_OK):
                fileobj = None

                if flag == "w":
                    if not (os.path.exists(filename) and os.path.isfile(filename)):
                        raise FileNotFoundError("File " + str(filename) + " does not exist")


                if fmt == "csv":
                    fileobj = open(filename, "r", newline="")
                else:
                    fileobj = open(filename, "rb" if self.fmt == "pickle" else "r")
                with fileobj:
                    self.load(fileobj)
        
        # old code, silent pls
        # super(dict).__init__(*args, **kwds)
        # dict.__init__(self, *args, **kwds)

    def sync(self, **kwargs):
        'Write dict to disk'
        iskilled=False
        passkey=kwargs.get("passkey",None)
        if 'killed' in kwargs:
            iskilled=kwargs['killed']

        if not self.filename:
            if iskilled and passkey==self.__accesskey:
                return False
            else:
                raise ValueError("Filename is not set")

        if self.flag == 'r':
            raise ValueError("Database is opened readonly")
        
        filename = self.filename
        tempname = ""
        random.seed(f"{str(os.urandom(32))}{str(datetime.datetime.now())}")

        # loop until that fulename does not exist
        while os.path.exists(tempname or filename):
            tempname = filename + ".tmp-" + str(random.randint(0, 9999999))

        fileobj = None
        if self.fmt == "csv":
            fileobj = open(tempname, "w", newline="")
        else:
            fileobj = open(tempname, 'wb' if self.fmt=='pickle' else 'w')
        try:
            with fileobj:
                self.dump(fileobj)
        except Exception:
            os.remove(tempname)
            raise
        shutil.move(tempname, self.filename)    # atomic commit
        if self.mode is not None:
            os.chmod(self.filename, self.mode)

    def close(self):
        ''' Close the database.'''
        self.sync(killed=True, passkey=self.__accesskey)

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.close()

    def __del__(self):
        self.close()

    def __deepcopy__(self, requesteddeepcopy):
        import copy
        return copy.deepcopy(dict(self))

    def setfname(self, filename):
        '''Set the filename

        Set to None to make a memory db
        '''
        self.filename = filename

    def getfname(self):
        '''Get the filename
        
        If null (more like None), then it is a memory db
        '''
        return self.filename

    def getfmt(self):
        '''Get the fmt
        
        '''
        return self.fmt

    def setfmt(self, fmt, /):
        '''Set the fmt
        
        '''
        # validate fmt
        self.__fmt_validator__(fmt)
        self.fmt = fmt

    def dump(self, fileobj):
        'Dump the dict to disk'
        # validate the fmt
        self.__fmt_validator__(self.fmt)

        if self.fmt == 'csv':
            csv.writer(fileobj).writerows(self.items())
        elif self.fmt == 'json':
            json.dump(self, fileobj, separators=(',', ':'), indent=4, ensure_ascii=True)
        elif self.fmt == 'pickle':
            pickle.dump(dict(self), fileobj, self.pickleopts['protocol'])
        elif inspect.isclass(self.fmt) and issubclass(self.fmt, SpoolDBAbstractBackend):
            self.fmt.dump(self, fileobj)
        else:
            raise NotImplementedError('Unknown fmt: ' + repr(self.fmt))

    def load(self, fileobj):
        'load dict from disk'
        # validate the fmt
        self.__fmt_validator__(self.fmt)

        # try fmts from most restrictive to least restrictive
        for loaderset in ((pickle.load, "pickle"), (json.load, "json"), (csv.reader, "csv"), (self.fmt, "AbstractBackend")):
            fileobj.seek(0)
            try:
                if loaderset[1] != "csv":
                    return self.update(loaderset[0](fileobj))
                elif loaderset[1] != "AbstractBackend":
                    d = dict()
                    for k, v in loaderset[0](fileobj):
                        d[k] = v
                    return self.update(d)
                else:
                    return self.update(loaderset[0].load(fileobj))
            # except Exception as e:
            except Exception:
                # print(f"{str(loaderset)}: {str(e)}")
                # no say this
                pass
        raise ValueError('File not in a supported fmt')

    def xget(self, key, default=None):
        '''Get a value from the dict, but throws.'''
        try:
            return self[key]
        except KeyError:
            if default: return default
            else: self.__missing__(key)

    def isJSONSerializable(self):
        '''Check if the dict is serializable/safe to serialize by JSON'''
        try:
            json.dumps(self)
            return True
        except TypeError:
            return False

    def __fmt_validator__(self, fmt):
        """Validate fmt"""
        # Broken
        # try:
        #     print(type(fmt))
        #     if issubclass(fmt, SpoolDBAbstractBackend):
        #         return fmt
        # except TypeError:
        #     pass
        
        if fmt in ('csv', 'json', 'pickle'):
            return fmt
        elif inspect.isclass(fmt) and issubclass(fmt, SpoolDBAbstractBackend):
            return fmt
        else:
            raise ValueError('Unknown fmt: ' + repr(fmt))



    def __repr__(self):
        return repr(dict(self))

    def __missing__(self, key):
        raise KeyError("Key not found: " + str(key))

    def __hash__(self):
        """Makes it possible that you can use this class as a dictionary key"""
        return hash((tuple(self.items()), tuple(self)))

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)




    @staticmethod
    def whichformat(filename):
        try:
            with open(filename, "rb") as f:
                pickle.load(f)
                return "pickle"
        except Exception:
            try:
                with open(filename, "r") as f:
                    json.load(f)
                    return "json"
            except Exception:
                try:
                    with open(filename, "r") as f:
                        csv.reader(f)
                        return "csv"
                except Exception:
                    raise ValueError("File not in a supported fmt")