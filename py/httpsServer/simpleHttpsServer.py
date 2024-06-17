
import http.server
import ssl
import socket

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/rw/rapid/execution':
            self.send_response(200)
            self.send_header('Content-type', 'application/hal+json;v=2.0')
            self.end_headers()
            self.wfile.write(b'{"_links":{"base":{"href":"http://127.0.0.1:80/rw/rapid/"},"self":{"href":"execution"}},"status":{"code":294912},"state":[{"_type":"rap-execution","_title":"execution","ctrlexecstate":"stopped","cycle":"forever"}]}')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Path not found')

def run(server_class=http.server.HTTPServer, handler_class=RequestHandler, port=443):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.socket = ssl.wrap_socket(httpd.socket, 
                                   server_side=True, 
                                   certfile='server.pem', 
                                   keyfile='server.key', 
                                   ssl_version=ssl.PROTOCOL_TLS)
    print(f'Starting HTTPS server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
