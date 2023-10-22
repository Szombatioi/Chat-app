#GUI Wrapper for GUI Class

import tkinter as tk
import GUIClass

class GUI:
    def __init__(self, name: str) -> None:
        self.gui = GUIClass.GUIClass(name)

        self.window = tk.Tk()
        self.window.title(f"Chat app - {self.gui.name}")
        self.window.geometry("600x500")

        self.frame = tk.Frame(self.window)
        self.frame.pack(side=tk.LEFT, anchor="n")

        #.pack()
        
    def addText(self, msg: str):
        tk.Label(self.frame, text=msg, anchor="w").pack()
        #ALIGN
        
    def startWindow(self):
        self.window.mainloop()
        
        
        

