import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 12345))

print("UDP Server is waiting for messages...")

while True:
    msg, addr = server.recvfrom(1024)
    msg = msg.decode()

    if msg.lower() == "exit":
        break

    print("Client:", msg)
    reply = input("Server: ")
    server.sendto(reply.encode(), addr)

    if reply.lower() == "exit":
        break

server.close()