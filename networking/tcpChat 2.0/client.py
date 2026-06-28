import threading
import socket

nickname = input("Choose a nickname: ")
if nickname == "admin":
    password = input("Enter password for admin: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 6769))

stop_thread = False

def receive():
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
                next_message = client.recv(1024).decode('ascii')
                if next_message == 'PASS':
                    client.send(password.encode('ascii'))
                    if client.recv(1024).decode('ascii') == 'REFUSE':
                        print("Connection was refused! Wrong password!")
                        stop_thread = True
                elif next_message == "BAN":
                    print("Connection refused due to ban!")
                    client.close()
                    stop_thread = True
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        if stop_thread == True:
            break
        message = f"{nickname}: {input('> ')}"
        if message.split(": ", 1)[1].startswith('/'):
            command = message.split(": ", 1)[1]
            if command.startswith('/kick'):
                target = command[6:].strip()
                client.send(f"KICK {target}".encode('ascii'))
            elif command.startswith('/ban'):
                target = command[5:].strip()
                client.send(f"BAN {target}".encode('ascii'))
            else:
                print("Commands can only be executed by the admin!")
        else:
            client.send(message.encode("ascii"))

receive_thread = threading.Thread(target=receive)
write_thread = threading.Thread(target=write)

receive_thread.start()
write_thread.start()
