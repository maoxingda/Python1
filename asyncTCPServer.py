import socket
import threading
import socketserver


class ThrdTCPReqHdr(socketserver.BaseRequestHandler):
    def handle(self):
        # data = self.request.recv(1024)
        self.request.sendall(threading.current_thread().name.encode())


class ThrdTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == '__main__':
    host, port = 'localhost', 18581

    server = ThrdTCPServer((host, port), ThrdTCPReqHdr)

    with server:
        server_thrd = threading.Thread(target = server.serve_forever)
        server_thrd.start()
        server_thrd.join()
