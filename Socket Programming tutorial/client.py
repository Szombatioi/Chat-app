# echo-client.py

#TODO: send multi line message  (if input only enter, then stop joining the messages)
    #1 message, not multiple

import socket

inp = input("Load file? y/n\n")
loadFile = False
if inp.lower() == 'y':
    loadFile = True
elif inp.lower() != 'n':
    exit(69420)

HOST = ''
PORT = ''
username = ''

array = [HOST, PORT, username]

if loadFile:
    with open('.config') as file:
        i = 0
        for line in file:
            line = line.strip()
            if(line):
                array[i] = line
                i+=1
        

        #TODO: *pukes* *puuuukes*
        HOST = array[0]
        PORT = int(array[1])
        username = array[2]
            

else:
    HOST = input("Enter host: ") #HOST = "152.66.181.95"  # The server's hostname or IP address
    PORT = int(input("Enter port: ")) #PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    if username == '':
        username = input("Enter username: ")
    print(f"Connected as {username}")
    while True:
        temp = input("$ ")
        msg = f"{username}: " + temp
        msg = bytes(msg, 'utf-8')
        if msg == "":
            break
        s.sendall(msg)

        data = s.recv(1024)

        #print(f"Received {data!r}")
        print(f"{data.decode('utf-8')}")