"""
HTTP server and request handler
"""
import json
from db import * # TODO: will implement soon
from utils import * # TODO: will implement soon
from urllib.parse import parse_qs, urlparse
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8080
HOST = "localhost"

class ToDoListServer(BaseHTTPRequestHandler):

    def do_GET(self):

        print(f"the path = {self.path}")
        print(f"the header = {self.headers}")
        myURL = urlparse(self.path)
        myQu = parse_qs(myURL.query)

        with open("./static/index.html", "r") as f:
            htmlData = f.read()

        with open("./static/style.css", "r") as f:
            cssData = f.read()

        if self.path == "/":
            self.send_response(200, "Thats Very Good. :)")
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write(htmlData.encode())

        elif self.path == "/tasks":
            self.send_response(200, "Thats Very Good. :)")
            self.send_header("content-type", "text/html")
            self.end_headers()

        elif self.path == "/tasks?":
            ...

        elif self.path == "/style.css":
            self.send_response(200, "Thats Very Good. :)")
            self.send_header("content-type", "text/css")
            self.end_headers()
            self.wfile.write(cssData.encode())

        elif self.path == "/favicon.ico":
            ...

        else:
            self.send_response(404, "Fuck HTTP")
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write("Error The page Not Found.".encode())

    def do_POST(self):

        if self.path == "/tasks":
            self.send_response(201, "Created")
            contant_lenght = self.headers["content-length"]
            print(contant_lenght)
            jsonData = self.rfile.read(int(contant_lenght)).decode()
            dictData = json.loads(jsonData)
            # TODO: use dict data to Create new task at the db by using also function from db.py

    def do_PUT(self):
        ...

    def do_DELETE(self):
        ...


try:
    with HTTPServer((HOST, PORT), ToDoListServer) as myServer:
        print(f"Start the server at http://{HOST}:{PORT}/")
        myServer.serve_forever()
except KeyboardInterrupt:
    print("\n\nServer is closed.")
