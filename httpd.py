import http.server
import socketserver
import urllib.request
import urllib.parse

PORT = 18580


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(http.HTTPStatus.OK)
        self.end_headers()

        urlparse = urllib.parse.urlparse(self.path)

        urlquery = urllib.parse.parse_qs(urlparse.query)

        if "/happyPk/match/anchorRank" == urlparse.path:
            anchor_id = urlquery["anchorId"][0]
            if "367566" == anchor_id:
                self.wfile.write('{"content":{"id":367566,"rank":5,"score":56501,"level":8,"levelName":"战神"},'
                                 '"state":0}'.encode(encoding = "utf-8"))
            else:
                self.wfile.write('{"code":"unreachable"}'.encode(encoding = "utf-8"))
        elif "/hero/rank/hero" == urlparse.path:
            self.wfile.write('{"retcode":0,'
                             '"result":{"run-time":0,"state":1,"qs":385985,"residueTime":144821,"msg":"获得成功了",'
                             '"isShow":false,"info":{"userId":0,"anchorId":0,"amount":0,"roomId":0,'
                             '"userNickName":"齐齐达人","anchorNickName":"齐齐达人"}}}'.encode(encoding = "utf-8"))
        else:
            self.wfile.write('{"code":"unreachable"}'.encode(encoding = "utf-8"))


Handler = http.server.SimpleHTTPRequestHandler
# Handler = MyHandler

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
