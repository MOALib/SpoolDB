import spooldb, os

if __name__ == "__main__":
    print("Example program\n\n")
    pklpath = "test.db"
    widepklpath = "testw.db"
    csvpath = "test2.csvdb"
    jsnpath = "test3.jsondb"
    shelfp = "shelf.shelf"
    adb = "abstractdb.adb"

    if not os.path.isfile(pklpath):
        with open(pklpath, "wb") as f:
            f.write(b"")

    if not os.path.isfile(csvpath):
        with open(csvpath, "w") as f:
            f.write("")

    if not os.path.isfile(shelfp):
        with open(shelfp, "w") as f:
            f.write("")

    if not os.path.isfile(jsnpath):
        with open(jsnpath, "w") as f:
            f.write("")

    if not os.path.isfile(adb):
        with open(adb, "w") as f:
            f.write("")

    with spooldb.SpoolDB(pklpath, flag='c', fmt="pickle") as db:
        import random
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

        for i in range(0, 5):
            db[i] = i

        db["random"] = random.random()

        # db.load(open(pklpath, "rb"))

    with spooldb.open(csvpath, flag='c', fmt="csv") as db:
        with spooldb.open(pklpath, flag='c', fmt="pickle") as db2:
            db.update(db2)

    with spooldb.open(jsnpath, flag='c', fmt="json") as jsndb:
        with spooldb.open(csvpath, flag='c', fmt="csv") as csvdb:
            jsndb.update(csvdb)

    with spooldb.openshelve(shelfp) as shelfdb:
        with spooldb.open(jsnpath, flag='c', fmt="json") as jsndb:
            shelfdb.update(jsndb)

    with spooldb.openshelve(shelfp) as shelfdb:
        for i, o in shelfdb.items():
            print(f"{i}:{o}")

    if False: # ignore until it gets better
        class SDBA(spooldb.SpoolDBAbstractBackend):
            def load(self, fileobj):
                o = fileobj.read()
                d = dict()
                # split by line
                lines = []
                for line in o.splitlines(): lines.append(line)

                # split by =
                for line in lines:
                    key, value = line.split("=")
                    d[key] = value

                return o

            def dump(self, data, fileobj):
                for key, value in data.items():
                    fileobj.write(f"{key}={value}\n")


        with spooldb.open(adb, flag='c', fmt=SDBA()) as asdb:
            asdb["test"] = "test"
