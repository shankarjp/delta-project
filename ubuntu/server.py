import os
import socket
import threading
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 5023
ADDR = (IP, PORT)
SIZE = 1024

cwd = os.getcwd()
SERVER_DATA_PATH = os.path.join(cwd, "server_data")

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    conn.send("Welcome to Stego File Server!".encode("utf-8"))
    while True:
        raw_data = conn.recv(SIZE).decode("utf-8")
        mod_data = raw_data.split("@")
        cmd = mod_data[0]
        if cmd == "LOGOUT":
            break
        elif cmd == "HELP":
            conn.send("Help Message".encode("utf-8"))
        elif cmd == "SEND":
            print(f"[MESSAGE] {addr} {mod_data[1]}")
            conn.send("Message Received!".encode("utf-8"))
        elif cmd == "DOWNLOAD":
            file_name = mod_data[1]
            file_path = os.path.join(SERVER_DATA_PATH, file_name)
            if os.path.isfile(file_path):
                conn.send(f"FOUND@{str(os.path.getsize(file_path))}".encode("utf-8"))
                time.sleep(0.01)
                f = open(file_path, "rb")
                while True:
                    data = f.read(SIZE)
                    if data:
                        conn.send(data)
                    else:
                        f.close()
                        break
            else:
                conn.send(f"NOTFOUND".encode("utf-8"))
        elif cmd == "UPLOAD":
            response = conn.recv(SIZE).decode("utf-8")
            response = response.split("@")
            if response[0] == "FOUND":
                time.sleep(0.01)
                file_size = response[1]
                file_name = mod_data[1]
                file_path = os.path.join(SERVER_DATA_PATH, file_name)
                f = open(file_path, "wb")
                data = conn.recv(SIZE)
                total_recv = len(data)
                f.write(data)
                while total_recv < file_size:
                    data = conn.recv(SIZE)
                    total_recv += len(data)
                    f.write(data)
                f.close()
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

