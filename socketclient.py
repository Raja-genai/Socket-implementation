import socket

try:
    c = socket.socket()
    c.connect(('1xx.xxx.x.x', 13000))  # Replace with server's actual IP

    print("Connected to server. Type 'bye' to exit.")

    while True:
        message = input("You: ")
        c.send(message.encode())
        if message.lower() == "bye":
            break
        reply = c.recv(1024).decode()
        print("Server:", reply)

    c.close()

except Exception as e:
    print("Connection failed:", e)
