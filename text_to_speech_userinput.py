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
    # text = input("Enter the text")
    text = open("demo.text",mode="r").read()
    output = gTTS(text,lang='en',slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')


texttospeech()
