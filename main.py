import time
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "10.184.187.96"
PORT = 8000

class HTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Hello world</h1></body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time:" "' + date + '"}', "utf-8"))


server = HTTPServer((HOST, PORT), HTTP)
print("Server running")
server.serve_forever()
server.server_close()
print("Server stopped")
