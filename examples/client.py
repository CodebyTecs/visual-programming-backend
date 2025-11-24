import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8080
client_socket.connect((host, port))

message = "Hello, World!"
client_socket.send(message.encode())

data = client_socket.recv(1024).decode()
print(f"Получено от сервера: {data}")

client_socket.close()
