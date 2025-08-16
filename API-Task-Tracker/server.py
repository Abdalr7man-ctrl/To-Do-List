"""
HTTP server and request handler
"""
from urllib.parse import parse_qs, urlparse
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8080
HOST = "localhost"

class Server(BaseHTTPRequestHandler):


    def do_GET(self):
        ...

    def do_POST(self):
        ...

    def do_PUT(self):
        ...

    def do_DELET(self):
        ...

with HTTPServer(HOST, PORT, Server) as myServer:
    print(f"Start the server at http://{HOST}:{PORT}/")
    myServer.serve_forever()
