import socket

servername = "Server of Aryan"
servernum = 17
port = 5050

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind(('', port))
serversock.listen(1)

print(f"'{servername}' is listening on port {port}")

while True:
    conn, addr = serversock.accept()
    data = conn.recv(1024).decode()

    clientname, clientnumstr = data.split(',')
    clientnum = int(clientnumstr)

    if not 1 <= clientnum <= 100:
        print("Received number out of range. Server shutting down.")
        break
    
    print("\nConnection On")
    print(f"Client’s name: {clientname}")
    print(f"Server’s name: {servername}")
    print(f"Client’s integer: {clientnum}")
    print(f"Server’s integer: {servernum}")
    print(f"The sum: {clientnum + servernum}")

    response = f"{servername},{servernum}"
    conn.send(response.encode())
    conn.close()

serversock.close()
print("Server is offline.")