import socket

#TODO: handle multiple connections
#TODO: 2 threads for sending and recieving


#HOST = socket.gethostbyname(socket.gethostname())  # Standard loopback interface address (localhost) -> can be hostname, IP address (IPv4 format) or empty string (accepts connection on every IPv4 interface)
HOST = "192.168.56.1"
PORT = 6969  # Port to listen on (non-privileged ports are > 1023)

run = True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #sockets support context manager type (use with)
    #AF_INET -> address family for IPv4
    #SOCK_STREAM -> socket type for TCP

    s.bind((HOST, PORT)) #associate the socket with a specific network interface & port number (w/ a tuple!)
    print("Waiting for connection")
    s.listen() #enables server to accept connections ("listening socket")
    conn, addr = s.accept() #accept blocks and waits for a connection (and return its values)
    with conn: #conn is a socket, that communicates with the connected client
        print(f"Connected by {addr}")
        
        #? thread
        
        while run:
            data = conn.recv(1024)
            if data:
                print(f"{data.decode('utf-8')}")
            
            inp = input("$ ")
            if inp == "exit":
                print("exiting")
                run = False
                break
            else:
                msg = f"*server*: " + inp
                msg = bytes(msg, 'utf-8')
                if msg is None:
                    break
                conn.sendall(msg)
input("Press anything to exit")
