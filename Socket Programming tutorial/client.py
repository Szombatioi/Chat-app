import socket
import threading
import GUI

#todo: send multi line message  (if input only enter, then stop joining the messages)
    #send in 1 message, not multiple

import run

HOST = ''
PORT = ''
USERNAME = ''

array = [HOST, PORT, USERNAME]

msgQueue = []
dataQueue = []
Runner = run.Run() #run = True

def sendMsgThread(runner: run):
    while runner.getRun():
        inp = input('$ ')
        if inp == "exit":
            print("exiting")
            runner.stop()
            break
        msg = bytes(f"{USERNAME}: {inp}", 'utf-8')
        msgQueue.append(msg)

def getDataThread(runner: run, s: socket):
    while runner.getRun():
        try:
            data = s.recv(1024)
            if data.strip() is not None:
                dataQueue.append(data)
        except ConnectionAbortedError:
            print("Server closed the connection")
            runner.stop()

def manageThread(s: socket, gui: GUI):
    while Runner.getRun():
        if msgQueue.__len__() > 0:
            _msg = msgQueue.pop(0)
            s.sendall(_msg)
            gui.addText(_msg)

        if dataQueue.__len__() > 0:
            _msg = dataQueue.pop(0).decode('utf-8')
            print(_msg)
            gui.addText(_msg)





try:
    with open('.config') as file:
        i = 0
        for line in file:
            line = line.strip()
            if(line):
                array[i] = line
                i+=1
        #todo: *pukes* *pukes more*
        HOST, PORT, USERNAME = array
        PORT = int(PORT)
except FileNotFoundError:
    #HOST = input("Enter host: ") #HOST = "152.66.181.95"  # The server's hostname or IP address
    HOST = socket.gethostbyname(socket.gethostname())
    #PORT = int(input("Enter port: ")) #PORT = 65432  # The port used by the server
    PORT = 6969
    USERNAME = input("Enter username: ") #todo: check if username is empty

gui = GUI.GUI(USERNAME)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected as {USERNAME}")
    
    #? thread
    t1 = threading.Thread(target=sendMsgThread, args=(Runner, ))
    t2 = threading.Thread(target=getDataThread, args=(Runner, s,))
    t3 = threading.Thread(target=manageThread, args=(s, gui,))
    
    threads = [t1,t2,t3]
    for t in threads:
        t.start()
    
    
    gui.startWindow()
    
for t in threads:
    t.join()

input("Press anything to exit")