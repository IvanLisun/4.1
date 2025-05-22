from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Kubernetes!")

if __name__ == "__main__":
    server = HTTPServer(("", 80), Handler)
    print("Starting server...")
    server.serve_forever()
