from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import requests
import os

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        
        self._set_response()
        path = str(self.path)
        
        e_url = os.environ['URL']
        email = os.environ['EMAIL']
        bearer = os.environ['BEARER']

        if str(self.path).startswith('/?eml='+email +'&v=9'):
            logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
            url = e_url + "/api/torque"+path.replace("/","")
            headers = {"Authorization": "Bearer "+ bearer}
            response = requests.request("GET", url, headers=headers)
            print(response.status_code)
            print(response.text)
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=8081):

    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    if not ("URL" in os.environ or "EMAIL" in os.environ or "BEARER" in os.environ):
        logging.info("Missing environment variables!\nStopping server")
        httpd.server_close()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    run(port=8081)