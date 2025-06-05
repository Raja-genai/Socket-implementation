# Python Socket Chat (Client-Server)

A simple Python socket programming project that enables real-time client-server communication over a LAN using IP-based connections. This was developed as part of my internship learning to understand sockets and continuous data transmission in Python.

---

## 🔧 Features

- Connect over LAN using server's IP address
- Continuous message flow between client and server
- Graceful exit with "bye"
- Handles multiple message exchanges without reconnecting

---

## 📁 File Structure

- `socketserver.py` — Runs on the server machine; listens for incoming client connections and exchanges messages.
- `socketclient.py` — Connects to the server; sends and receives messages continuously.

---

## ▶️ How to Run

### On the **Server** device:
```bash


python3 socketserver.py

📌 Notes
	•	Use Ctrl + C to stop the server manually.
	•	Make sure the server IP and port are accessible through the firewall.
	•	Tested on macOS terminal and works for two devices on the same network.
