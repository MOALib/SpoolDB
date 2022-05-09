#!/bin/env python3
# static http server
import http.server, os, socket

def getport():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port

def serve(port, path):
    os.chdir(path)
    http.server.SimpleHTTPRequestHandler.extensions_map['.wasm'] = 'application/wasm'
    http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=port)