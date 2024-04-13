from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # レスポンスヘッダーを送信
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # HTMLコンテンツを生成して送信
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Python HTTP Server</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple HTML page served by Python's http.server.</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

def server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()
