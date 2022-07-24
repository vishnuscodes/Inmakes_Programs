from tkinter import *
import tkinter as tk

field_text = ""

def add_to_field(sth):
    global field_text
    field_text=field_text+str(sth)
    field.delete("1.0","end")
    field.insert("1.0",field_text)


def calculatefield():
    global field_text
    result = str(eval(field_text))
    field.delete('1.0', END)
    field.insert('1.0',result)

def clear_content():
    global field_text
    field_text = ""
    field.delete('1.0', END)

window = Tk()
window.geometry("300x300")
field = tk.Text(window,height=2,width=37,font=("Times New Roman",12))
field.grid(row=1,column=1,columnspan=4)

onebutton = Button(window, text = "1", height= 2, width=1, command = lambda: add_to_field(1))
onebutton.grid(row=2,column=1,sticky="nsew")

twobutton = Button(window, text = "2", height= 3, width=1, command = lambda: add_to_field(2))
twobutton.grid(row=2,column=2,sticky="nsew")

threebutton = Button(window, text = "3", height= 3, width=1, command = lambda: add_to_field(3))
threebutton.grid(row=2,column=3,sticky="nsew")

multbutton = Button(window, text = "x", height= 3, width=1, command = lambda: add_to_field("*"))
multbutton.grid(row=2,column=4,sticky="nsew")

button4 = Button(window, text = "4", height= 3, width=1, command = lambda: add_to_field(4))
button4.grid(row=3,column=1,sticky="nsew")

button5 = Button(window, text = "5", height= 3, width=1, command = lambda: add_to_field(5))
button5.grid(row=3,column=2,sticky="nsew")

button6 = Button(window, text = "6", height= 3, width=1, command = lambda: add_to_field(6))
button6.grid(row=3,column=3,sticky="nsew")

buttonadd = Button(window, text = "+", height= 3, width=1, command = lambda: add_to_field("+"))
buttonadd.grid(row=3,column=4,sticky="nsew")

button7 = Button(window, text = "7", height= 3, width=1, command = lambda: add_to_field(7))
button7.grid(row=4,column=1,sticky="nsew")

button8 = Button(window, text = "8", height= 3, width=1, command = lambda: add_to_field(8))
button8.grid(row=4,column=2,sticky="nsew")

button9 = Button(window, text = "9", height= 3, width=1, command = lambda: add_to_field(9))
button9.grid(row=4,column=3,sticky="nsew")

buttonsub = Button(window, text = "-", height= 3, width=1, command = lambda: add_to_field("-"))
buttonsub.grid(row=4,column=4,sticky="nsew")

button0 = Button(window, text = "0", height= 3, width=1, command = lambda: add_to_field(0))
button0.grid(row=5,column=1,sticky="nsew")

buttondot = Button(window, text = ".", height= 3, width=1, command = lambda: add_to_field("."))
buttondot.grid(row=5,column=2,sticky="nsew")

buttoncalc = Button(window, text = "=", height= 3, width=1, command = calculatefield)
buttoncalc.grid(row=5,column=3,sticky="nsew")

buttonclear = Button(window, text = "Clear", height= 3, width=1, command = clear_content)
buttonclear.grid(row=5,column=4,sticky="nsew")

window.mainloop()

