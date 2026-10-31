from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse,parse_qs
from configparser import ConfigParser
config=ConfigParser()
config.read("codes.ini")



class MyHandler(BaseHTTPRequestHandler):
    code=None
    def do_GET(self):
        parsed_url=urlparse(self.path)

        params=parse_qs(parsed_url.query)
        if "code" in params:
            MyHandler.code=params["code"][0]
            print("Authorization code received!")
            # print("Authorization code:", MyHandler.code)
            config["LINKEDIN"]["access_code"]=MyHandler.code
            with open("codes.ini", "w") as file:
                config.write(file)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Authorization successful! You can close this tab.")

        # self.server.shutdown()
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Authorization code not found in the request.")

server=HTTPServer(("localhost",8000),MyHandler)
print("Waiting for LinkedIn authorization...")
# print(MyHandler.code)
# print("Authorization code:?", MyHandler.code)

server.serve_forever()
