
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server

import os
directory = os.getcwd()
import socket

PORT = 8080
ip = "0.0.0.0"


f_choise = input('what want to share File: f or Text: t\n')

if f_choise =='f':
    from tkinter import filedialog
    import tkinter as tk
    root = tk.Tk()
    root.withdraw ()
    path = filedialog.askdirectory()
    path = path.replace('/', '\\')

    class requestHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=path, **kwargs)
    def main():
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname) 

        server_address = (ip, PORT)
        server = HTTPServer(server_address, requestHandler)
        print(f'Server running on ip {IPAddr}, port {PORT}')
        server.serve_forever()


    
    main()



elif f_choise == 't':
    # text_to_shaire = input('write tha text blow:\n')
    import sys
    msg = sys.stdin.readlines()
    text_to_shaire = str(msg).replace('[', '').replace(']', '').replace("'", '').replace('"', '').replace('\\n', '\n').replace(',', '')

    class requestHandler(BaseHTTPRequestHandler) :
        def do_GET(self) :
            if self.path.endswith('/e'):
                quit()
            else:
                self.send_response(200)
                self.send_header('content-type' , 'text/html')
                self.end_headers()
                Output = ''
                # Output += '<h1>%s</h1>'% text_to_shaire
                Output +=f'''
                <html><body>

                <h2>Text sheard is </h2>
                <textarea cols="60" rows="13">{text_to_shaire}</textarea><br>

                <a href="e">exit</a>
                </body></html>
                '''
                self.wfile.write(Output.encode( ))
    def main():
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname) 

        server_address = (ip, PORT)
        server = HTTPServer(server_address, requestHandler)
        print(f'Server running on ip {IPAddr}, port {PORT}')
        server.serve_forever()


    
    main()
