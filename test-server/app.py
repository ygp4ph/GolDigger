import http.server
import socketserver

PORT = 5000

class TestHandler(http.server.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        # We need to not write body for HEAD requests, but it's simpler to just write it if we can
        # but the request handler might fail if we write body to a HEAD request.
        # So let's check self.command
        is_head = self.command == 'HEAD'

        def write_response(status, content_type, body_bytes):
            self.send_response(status)
            self.send_header("Content-type", content_type)
            self.end_headers()
            if not is_head:
                self.wfile.write(body_bytes)

        if self.path == '/':
            write_response(200, "text/html", b"""
            <html>
                <body>
                    <h1>Test Server</h1>
                    <a href="/about">About</a>
                    <a href="/contact">Contact</a>
                    <a href="http://external.example.com/test">External Link</a>
                </body>
            </html>
            """)
        elif self.path == '/about':
            write_response(200, "text/plain", b"About")
        elif self.path == '/contact':
            write_response(200, "text/plain", b"Contact")
        elif self.path == '/robots.txt':
            write_response(200, "text/plain", b"""User-agent: *
Disallow: /admin
Allow: /hidden-file
Sitemap: http://127.0.0.1:5000/custom-sitemap.xml
""")
        elif self.path == '/sitemap.xml':
            write_response(200, "application/xml", b"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>http://127.0.0.1:5000/sitemap-page-1</loc>
   </url>
   <url>
      <loc>http://127.0.0.1:5000/sitemap-page-2</loc>
   </url>
</urlset> """)
        elif self.path == '/custom-sitemap.xml':
            write_response(200, "application/xml", b"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>http://127.0.0.1:5000/custom-sitemap-page</loc>
   </url>
</urlset> """)
        else:
            write_response(200, "text/plain", b"OK")

    def log_message(self, format, *args):
        # print("%s - - [%s] %s\n" %
        #      (self.client_address[0],
        #       self.log_date_time_string(),
        #       format%args))
        pass

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

with ReusableTCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
