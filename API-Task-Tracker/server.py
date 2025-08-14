"""
HTTP server and request handler
"""
from urllib.parse import parse_qs, urlparse
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8080
HOST = "localhost"
