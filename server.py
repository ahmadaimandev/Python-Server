from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "192.168.0.185"
PORT = 8080
#define class
class httpserver(BaseHTTPRequestHandler):
    def do_GET(self):
        #essentially responds to get request
        self.send_response(200)
        
        self.send_header("Content-Type", "text/html")
        
        self.end_headers()
        
        self.wfile.write(bytes("<html><body></body><h1>HELLO WORLD!</h1></html", "UTF-8")) #This bytes have certain encoding
        
        server = HTTPServer((HOST,PORT), httpserver)
        print("Server Is Now Running....")
        
        server.serve_forever()
        server.server_close()
        
        print("Server Has Stopped....")