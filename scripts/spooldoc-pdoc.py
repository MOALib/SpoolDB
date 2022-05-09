#!/bin/env python3

import server3, os, sys, webbrowser, threading

def main():
    # add cwd to path
    sys.path.append(os.getcwd())

    sockport=server3.getport()

    try:
        os.system(f"pdoc spooldb --logo http://localhost:{sockport}/img/spooldb.png -o ./doc")
    except KeyboardInterrupt:
        # exit
        pass


    print(f"serving this directory on http://localhost:{sockport}")
    print(f"serving this doc on http://localhost:{sockport}/pdoc-doc/")
    # server3.serve(sockport, ".")
    threading.Thread(target=server3.serve, args=(sockport, "."), daemon=True).start()

    webbrowser.open(f"http://localhost:{sockport}/pdoc-doc/")
    while True:
        try:
            # wait until keyboardInterrupt
            pass
        except KeyboardInterrupt:
            # exit
            break


if __name__ == "__main__": main()
sys.exit(0)