import socket
from select import select

Sock_r =[]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))

def conn_soket(server_socket):
    client_sock, addr = server_socket.accept()
    Sock_r.append(client_sock)

def send_msg(input_socket):
    request = input_socket.recv(4096)
    if not request:
        input_socket.close()
    else:
        response = 'Hello world\n'.encode()
        input_socket.send(response)

def main():
    while True:
        read_f, _, _ = select(Sock_r, [],[])

        print(read_f)
        for sock in read_f:
            if sock is server_socket:
                conn_soket(sock)
            else:
                send_msg(sock)

if __name__ == '__main__':
    server_socket.listen()
    Sock_r.append(server_socket)
    main()
