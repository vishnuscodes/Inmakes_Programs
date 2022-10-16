from tkinter import *

import pyqrcode
import qrcode

from PIL import ImageTk,Image

root = Tk()

def GenerateQRCode():
    linkname = text1.get()
    link = text2.get()
    file_name = linkname+".png"
    custom_QR = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=4,
    )
    custom_QR.make(fit=True)
    custom_QR.add_data(link)
    qr=custom_QR.make_image()
    qr.save(file_name)
    img = Image.open(file_name)
    QRCodeImg = ImageTk.PhotoImage(img)
    QRCodeLabel = Label(image=QRCodeImg)
    QRCodeLabel.grid(row=4, column=2,pady=10)
    # image_label.image = image
    # image_label.grid(row=4, column=2, rowspan=5, sticky="w")

root.title("QR Code Generator")

root.geometry("400x500")

frame = Frame(root)

frame.columnconfigure(1,weight=1)
frame.columnconfigure(2,weight=3)

label1 = Label(root,text="Link Name")
label2 = Label(root,text="Enter the link")
text1 = Entry(root,width=40)
text2 = Entry(root,width=40)
button1 = Button(root,text="Generate QRCode",width=20,command=GenerateQRCode)
# label3 = Label(root,text="                      ")
# label4 = Label(root,text="                      ")

label1.grid(row=0,column=1,pady=10,padx=20)
label2.grid(row=1,column=1,pady=10,padx=20)
# label3.grid(row=0,column=0,pady=10)
# label4.grid(row=1,column=0,pady=10)
text1.grid(row=0,column=2,columnspan=4,sticky="w")
text2.grid(row=1,column=2,columnspan=4,sticky="w")
button1.grid(row=3,column=2,columnspan=5,sticky="w")
root.mainloop()