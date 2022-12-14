#!/usr/bin/env python3
import http.server
import socketserver
import os
import json
from urllib.parse import urlparse, parse_qs

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        path = urlparse(self.path)
        parse_args = parse_qs(path.query)

        print(self.path)
        
        if path.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()   

            if parse_args.get('str', None):
                text = parse_args.get('str', None)[0]
                lowercase = sum(1 for c in text if c.islower())
                uppercase = sum(1 for c in text if c.isupper())
                digits = sum(1 for c in text if c.isdigit())
                special_chars = sum(1 for c in text if not c.isdigit() and not c.isalpha())

                sumamry_json = {
                    'lowercase': lowercase,
                    'uppercase': uppercase,
                    'digits': digits,
                    'special': special_chars
                }
                self.wfile.write(str(sumamry_json).encode('utf-8'))
            
        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
