---

### 🖥️ `socketserver.py`

```python
import socket

s = socket.socket()
print("Socket Created")
s.bind(('0.0.0.0', 13000))
s.listen(3)
print("Waiting for connections")

while True:
    c, addr = s.accept()
    print("Connected with", addr)

    while True:
        try:
            data = c.recv(1024).decode()
            if not data or data.lower() == "bye":
                print(f"Client {addr} disconnected.")
                break
            print(f"Client: {data}")
            reply = input("Server: ")
            c.send(reply.encode())
        except:
            break

    c.close()
