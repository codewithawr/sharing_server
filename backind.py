
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server

import os
directory = os.getcwd()
import socket

PORT = 8080
ip = "0.0.0.0"


f_choise = input('what want to share File: f or Text: t\n')

def main():
    server_address = (ip, PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()



if f_choise =='f':
    from tkinter import filedialog
    import tkinter as tk
    root = tk.Tk()
    root.withdraw ()
    path = filedialog.askdirectory()
    path = path.replace('/', '\\')
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname) 
    print(IPAddr)
    # os.system(f'python -m http.server -d {path} {PORT}')
    

    class requestHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=path, **kwargs)
    
    main()



elif f_choise == 't':
    text_to_shaire = input('write tha text blow:\n')

    class requestHandler(BaseHTTPRequestHandler) :
        def do_GET(self) :
            if self.path.endswith('/e'):
                quit()
            else:
                self.send_response(200)
                self.send_header('content-type' , 'text/html')
                self.end_headers()
                Output = ''
                Output += '<htm ><body>'
                Output += '<input> </input>'
                Output += '<h1>%s</h1>'% text_to_shaire
                Output += '</body></html>'
                Output += '''
                <div class="container">
                <pre>
                Text in a pre element
                is displayed in a fixed-width
                font, and it preserves
                both spaces and
                line breaks.
                </pre>
                </div>
                '''
                Output += '<a href="e">exit</a>'
                self.wfile.write(Output.encode( ))
    
    main()
