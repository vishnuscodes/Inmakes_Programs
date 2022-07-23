from tkinter import *

class myweb:
    def __init__(self,root1):
        frame = Frame(root1)
        frame.pack()
        self.button1=Button(frame,text="OK",command=self.button1cmd)
        self.button1.pack()
        self.button2=Button(frame,text="Cancel",command=self.button2cmd)
        self.button2.pack()
        self.button3=Button(frame,text="Quit",command=frame.quit)
        self.button3.pack()

    def button1cmd(self):
        print("Clicked OK")

    def button2cmd(self):
        print("Clicked Cancel")


root = Tk()

mywebobj = myweb(root)
root.mainloop()