#!/usr/bin/env python3
import http.server
import socketserver
import os

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        
        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            
            self.wfile.write(b"Hello World!\n")
        else:
            super().do_GET()

    def count_chars(self, string):
        lowercase = sum(1 for c in string if c.islower())
        uppercase = sum(1 for c in string if c.isupper())
        digits = sum(1 for c in string if c.isdigit())
        special_chars = sum(1 for c in string if not c.isdigit() and not c.isalpha())
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
