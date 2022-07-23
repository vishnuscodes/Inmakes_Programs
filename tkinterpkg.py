from tkinter import *

root = Tk()

label1 = Label(root,text="Username")
label2 = Label(root,text="Password")

entry1 = Entry(root)
entry2 = Entry(root)

button1 = Button(root,text="Login")
button2 = Button(root,text = "Cancel")

label1.grid(row = 0,column = 0)
label2.grid(row = 1,column = 0)
entry1.grid(row = 0,column = 1)
entry2.grid(row = 1,column = 1)

button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
root.geometry("1000x1200")
root.mainloop()