import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Client: ")
    client.sendto(msg.encode(), ("127.0.0.1", 12345))

    if msg.lower() == "exit":
        break

    reply, addr = client.recvfrom(1024)
    print("Server:", reply.decode())

    if reply.decode().lower() == "exit":
        break

client.close()