import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8080
server_socket.bind((host, port))

server_socket.listen(10)

print(f"Сервер слушает на {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Подключено: {addr}")

    data = client_socket.recv(1024).decode()
    print(f"Получено от клиента: {data}")

    client_socket.close()
