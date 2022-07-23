from tkinter import *
root = Tk()
canvas=Canvas(root,width=100,height=200)
canvas.pack()
newcircle = canvas.create_oval(10,20,80,100,fill = "red")
root.mainloop()