#TODO: send multi line message  (if input only enter, then stop joining the messages)
    #1 message, not multiple

import socket

HOST = ''
PORT = ''
USERNAME = ''

array = [HOST, PORT, USERNAME]


try:
    with open('.config') as file:
        i = 0
        for line in file:
            line = line.strip()
            if(line):
                array[i] = line
                i+=1
        

        #TODO: *pukes* *pukes more*
        HOST, PORT, USERNAME = array
        PORT = int(PORT)
except FileNotFoundError:
    #HOST = input("Enter host: ") #HOST = "152.66.181.95"  # The server's hostname or IP address
    HOST = socket.gethostbyname(socket.gethostname())
    #PORT = int(input("Enter port: ")) #PORT = 65432  # The port used by the server
    PORT = 6969
    USERNAME = input("Enter username: ") #TODO: check if username is empty

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected as {USERNAME}")
    while True:
        msg = bytes(f"{USERNAME}: {input('$ ')}", 'utf-8')
        if msg.strip() is None:
            break
        s.sendall(msg)

        data = s.recv(1024)

        #print(f"Received {data!r}")
        print(f"{data.decode('utf-8')}")