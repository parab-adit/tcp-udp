import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))

while True:
    msg = input("Client: ")
    client.send(msg.encode())

    if msg.lower() == "exit":
        break

    reply = client.recv(1024).decode()
    print("Server:", reply)

    if reply.lower() == "exit":
        break

client.close()