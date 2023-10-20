import tkinter as tk
import time
import threading

window = tk.Tk("Client")
window.geometry("400x400+400+300")
#myFrame = tk.Frame(window, width=400, height= 400)


button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="black",
    fg="white",
    
)


button.pack()
#myFrame.pack()

run = True
def stopFn(event):
    run = False

button.bind("<Button-1>", stopFn)

#get message

def threadfunc():
    while run:
        tk.Label(text="Hello, Tkinter").pack()
        print(run)
        time.sleep(1)

# t1 = threading.Thread(target=threadfunc)
# t1.start()

# t1.join()
window.mainloop()


    