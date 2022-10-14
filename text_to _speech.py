from gtts import gTTS
import os
from tkinter import *

root = Tk()
root.geometry("250x200")
root.title("Text to speech converter")
root.resizable(0, 0)
frame = Frame(root)
frame.pack()


def texttospeech():
    text = text1.get()
    output = gTTS(text,lang='en',slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')


#root.columnconfigure(0,weight=1)
#root.columnconfigure(1,weight=3)

label1 = Label(frame,text="Enter the text")
label1.grid(column=0,row=0,pady=10,padx=5)

text1 = Entry(frame)
text1.grid(column=1,row=0,columnspan=4)

button1 = Button(frame,text="Convert To Audio",command=texttospeech)
button1.grid(column=1,row=3)

root.mainloop()
