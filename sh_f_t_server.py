
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server


PORT = 8080
ip = "0.0.0.0"

def main():
    # geting the Gateway of host
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IPAddr= s.getsockname()[0]

    server_address = (ip, PORT)
    server = HTTPServer(server_address, requestHandler)
    print(f'Server running on ip {IPAddr}, port {PORT}')
    server.serve_forever()

f_choise = input('what want to share File: f or Text: t\n')

if f_choise =='f':
    try:
        from tkinter import filedialog
        import tkinter as tk
        root = tk.Tk()
        root.withdraw ()
        path = filedialog.askdirectory()
        path = path.replace('/', '\\')
    except:
        path = input('error to open directory finder\ntype the path of folder heare:')

    class requestHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=path, **kwargs)

    
    main()


elif f_choise == 't':
    # text_to_shaire = input('write tha text blow:\n')
    if input('is it miltyline y/n :') == 'y':
        import sys
        print('write tha text blow : to end add ^Z to last line')
        import sys
        msg = sys.stdin.readlines()
        text_to_shaire = ''.join(str(i) for i in msg)
    else:
        text_to_shaire = input('write the singel line text blow :\n')

    class requestHandler(BaseHTTPRequestHandler) :
        def do_GET(self) :
            if self.path.endswith('/e'):
                quit()
            else:
                self.send_response(200)
                self.send_header('content-type' , 'text/html')
                self.end_headers()
                Output = ''
                Output +=f'''
                <html>
                    <body>
                        <h2>Text sheard is </h2>
                        <pre id="myInput" class="wp-block-code"><textarea rows="10" cols="50">{text_to_shaire}</textarea>'''
                Output +='''</pre>
                            <button class="k2-copy-button" id="k2button">Click to Copy</button>
                            <script>
                            function copyFunction() {
                            const copyText = document.getElementById("myInput").textContent;
                            const textArea = document.createElement('textarea');
                            textArea.textContent = copyText;
                            document.body.append(textArea);
                            textArea.select();
                            document.execCommand("copy");
                            k2button.innerText = "Code copied";
                                textArea.remove();
                            }
                            document.getElementById('k2button').addEventListener('click', copyFunction);
                            </script>
                        <br>
                        <br>
                        <a href="e">exit</a>
                    </body>
                </html>
                '''
                self.wfile.write(Output.encode( ))
    

    
    main()
