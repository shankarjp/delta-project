import os
import socket
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
    if(response == 'y' || response == 'Y'):
        while !connection:
            print("Verify Your Identity")
            user_name = input("username : ")
            user_password = input("password : ")
            if(db.CheckUser(user_name, user_password)):
                print("Login Successful\n")
                connection = True
            else:
                print("Login Failed\nTry Again\n")
    elif(response == 'n' || response == 'N'):
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
    print("Disconnected from the server")
    client.close()

if(__name__ == "__main__"):
    main()
