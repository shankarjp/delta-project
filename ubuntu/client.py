import os
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 5023
ADDR = (IP, PORT)
SIZE = 1024

cwd = os.getcwd()
SERVER_DATA_PATH = os.path.join(cwd, "server_data")
CLIENT_DATA_PATH = os.path.join(cwd, "client_data")

def pad(data):
    return data + ((16 - len(data)%16)*'{')

def pad_file(data):
    return data+((16 - len(data)%16)*b"\0")

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    connection = True
    while connection:
        info = client.recv(SIZE).decode("utf-8")
        print(f"{info}")
        raw_data = input("> ")
        mod_data = raw_data.split("@")
        cmd = mod_data[0]
        client.send(raw_data.encode("utf-8"))
        if cmd == "LOGOUT":
            break
    print("Disconnected from the server")
    client.close()

if(__name__ == "__main__"):
    main()
