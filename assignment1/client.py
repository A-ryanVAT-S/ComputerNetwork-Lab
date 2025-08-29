import socket

clientname = "Client of Aryan"
serverip = '127.0.0.1'
serverport = 5050
clientnum = 0

while True:
    userinput = input("Enter an integer between 1 and 100: ")
    try:
        clientnum = int(userinput)
        if 1 <= clientnum <= 100:
            break
        else:
            print("Number must be between 1 and 100.")
    except ValueError:
        print("That is not a valid number.")

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect((serverip, serverport))

message = f"{clientname},{clientnum}"
clientsock.send(message.encode())

data = clientsock.recv(1024).decode()
servername, servernumstr = data.split(',')
servernum = int(servernumstr)

print("\nReply:")
print(f"Client’s name: {clientname}")
print(f"Server’s name: {servername}")
print(f"Client’s integer: {clientnum}")
print(f"Server’s integer: {servernum}")
print(f"The sum : {clientnum + servernum}")

clientsock.close()