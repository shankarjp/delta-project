import os
import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 5023
ADDR = (IP, PORT)
SIZE = 1024

cwd = os.getcwd()
SERVER_DATA_PATH = os.path.join(cwd, "server_data")

def pad(data):
    return data + ((16 - len(data)%16)*'{')

def pad_file(data):
    return data + ((16 - len(data)%16)*b"\0")

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    conn.send("Welcome to Stego File Server!".encode("utf-8"))
    while True:
        data = conn.recv(SIZE).decode("utf-8")
        data = data.split("@")
        cmd = data[0]
        if cmd == "LOGOUT":
            break
        elif cmd == "HELP":
            conn.send("Help Message".encode("utf-8"))
        elif cmd == "SEND":
            print(f"[MESSAGE] {addr} {data[1]}")
            conn.send("Message Received!".encode("utf-8"))
        else:
            conn.send("Invalid Command!\n".encode("utf-8"))
    print(f"[DISCONNECTED] {addr} disconnected")
    conn.close()

def main():
    print("[STARTING] Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")

if(__name__ == "__main__"):
    main()

