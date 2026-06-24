import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1337))
s.listen()

for i in range(1, 11, 1):
    client, address = s.accept()
    print(f"({i}/10) Ping {address}")
    client.send(f"({i}/10) Pong".encode())
    client.close()
