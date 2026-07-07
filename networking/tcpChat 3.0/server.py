import socket, threading

host = '127.0.0.1'
port = 3000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]}: {message.decode('utf-8')}")
            broadcast(message)
        except:
            index = clients.index(client)
            nickname = nicknames[index]
            nicknames.remove(nickname)
            client.close()
            nickname = nicknames.index(client)
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        t = threading.Thread(target=handle, args=(client,))
        t.start()

print(f"Server running on port {port}...")
receive()
