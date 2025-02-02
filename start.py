buatkanfile README.txt import http.server
import socketserver

PORT = 5015
HOST = 'localhost'

# Membuat server HTTP
with socketserver.TCPServer((HOST, PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at {HOST}:{PORT}")
    httpd.serve_forever()
