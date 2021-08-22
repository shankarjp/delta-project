import os
import socket
import time
import scripts.db as db

IP = socket.gethostbyname(socket.gethostname())
PORT = 5023
ADDR = (IP, PORT)
SIZE = 1024

cwd = os.getcwd()
SERVER_DATA_PATH = os.path.join(cwd, "server_data")

def main():
    connection = False
    response = input("Do you have an account? (y/n) : ")
    if(response == 'y' or response == 'Y'):
        while !connection:
            print("Verify Your Identity")
            user_name = input("username : ")
            user_password = input("password : ")
            if(db.CheckUser(user_name, user_password)):
                print("Login Successful\n")
                connection = True
            else:
                print("Login Failed\nTry Again\n")
    elif(response == 'n' or response == 'N'):
        while !connection:
            print("Enter your Credentials")
            user_name = input("username : ")
            user_password = input("password : ")
            user_password_confirm = input("confirm password : ")
            if(user_password == user_password_confirm):
                if(db.CheckUser(user_name, user_password)):
                    print("Entered credentials already exists")
                    exit()
                else:
                    db.AddUser(user_name, user_password)
                    print("Registration Successful")
                    connection = True
            else:
                print("Passwords not matching\nTry Again\n")
    else:
        print("Invalid Entry")
        exit()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    CLIENT_DATA_PATH = os.path.join('/home/', CLIENT_GENERAL_PATH, user_name)
    while connection:
        info = client.recv(SIZE).decode("utf-8")
        print(f"{info}")
        raw_data = input("> ")
        mod_data = raw_data.split("@")
        cmd = mod_data[0]
        client.send(raw_data.encode("utf-8"))
        if cmd == "LOGOUT":
            break
        elif cmd == "DOWNLOAD":
            response = client.recv(SIZE).decode("utf-8")
            response = response.split("@")
            if(response[0] == "FOUND"):
                time.sleep(0.01)
                file_size = response[1]
                file_name = mod_data[1]
                file_path = os.path.join(CLIENT_DATA_PATH, file_name)
                f = open(file_path, "wb")
                data = client.recv(SIZE)
                total_recv = len(data)
                f.write(data)
                while total_recv < file_size:
                    data = client.recv(SIZE)
                    total_recv += len(data)
                    f.write(data)
                print(f"Downloaded {file_name}")
                f.close()
            else:
                print("File Not Found")
        elif cmd == "UPLOAD":
            file_name = mod_data[1]
            file_path = os.path.join(CLIENT_DATA_PATH, file_name)
            if os.path.isfile(file_path):
                client.send(f"FOUND@{str(os.path.getsize(file_path))}".encode("utf-8"))
                time.sleep(0.01)
                f = open(file_path, "rb")
                while True:
                    data = f.read(SIZE)
                    if data:
                        client.send(data)
                    else:
                        f.close()
                        print(f"Uploaded {file_name}")
                        break
            else:
                client.send(f"NOTFOUND")
    print("Disconnected from the server")
    client.close()

if(__name__ == "__main__"):
    main()
