from socket import *
from time import ctime

BUFSIZE = 1024

if __name__ == '__main__':
    sserver = socket(AF_INET, SOCK_STREAM)
    sserver.bind((u'localhost', 18580))
    sserver.listen(5)

    while True:
        (sclient, addr) = sserver.accept()
        msg = sclient.recv(BUFSIZE)
        while msg != b'quit':
            sclient.send(str.encode(ctime()))
            msg = sclient.recv(BUFSIZE)

        sclient.close()

    sserver.close()
