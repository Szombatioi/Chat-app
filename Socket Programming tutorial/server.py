import socket
import threading

#todo: handle multiple connections
#todo: Better console drawing (curses)

import run

msgQueue = []
dataQueue = []
Runner = run.Run() #run = True

#HOST = socket.gethostbyname(socket.gethostname())  # Standard loopback interface address (localhost) -> can be hostname, IP address (IPv4 format) or empty string (accepts connection on every IPv4 interface)
HOST = "192.168.56.1"
PORT = 6969  # Port to listen on (non-privileged ports are > 1023)
USERNAME = "*server*"

def sendMsgThread(runner: run):
    while runner.getRun():
        inp = input("$ ")
        if inp == "exit":
            print("exiting")
            runner.stop()
            break
        
        msg = bytes(f"{USERNAME}: {inp}", 'utf-8')
        msgQueue.append(msg)

def getDataThread(runner: run, conn):
    while runner.getRun():
        try:
            data = conn.recv(1024)
            dataQueue.append(data)
        except ConnectionResetError:
            print("Error occured, shutting down server")
            runner.stop()



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
        t1 = threading.Thread(target=sendMsgThread, args=(Runner,))
        t2 = threading.Thread(target=getDataThread, args=(Runner,conn,))
        
        t1.start()
        t2.start()
        
        while Runner.getRun():
            if msgQueue.__len__() > 0:
                conn.sendall(msgQueue.pop(0))

            if dataQueue.__len__() > 0:
                print(f"{dataQueue.pop(0).decode('utf-8')}")
t1.join()
t2.join()
input("Press anything to exit")
