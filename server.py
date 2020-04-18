import socket
import sys
import client

server_addr = ("localhost", 9000)

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.bind(server_addr)

while True:
    try:
        tcpsock.listen(5)
        print(" -> listening")
        client.Thread(*tcpsock.accept()).start()
    except KeyboardInterrupt:
        tcpsock.close()
        sys.exit()
