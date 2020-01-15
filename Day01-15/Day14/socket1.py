from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('127.0.0.1', 6789))
    server.listen(512)
    print('Server starting listen')
    while True:
        client, addr = server.accept()
        print(str(addr) + '連接到server')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()


if __name__ == '__main__':
    main()