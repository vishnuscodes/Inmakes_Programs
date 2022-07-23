from tkinter import *

root = Tk()
def commandfunc():
    Label(root,text="Command pressed").pack()

mymenu = Menu(root)

root.config(menu=mymenu)

filemenu = Menu(mymenu,tearoff=0)
mymenu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New Project",command= commandfunc)
localmenu = Menu(filemenu,tearoff=0)
filemenu.add_cascade(label="Local History",menu=localmenu)
localmenu.add_command(label="Show History",command= commandfunc)
localmenu.add_command(label="Put label...",command= commandfunc)
filemenu.add_command(label="Save",command= commandfunc)
filemenu.add_separator()
filemenu.add_command(label="Settings...",command= commandfunc)
filemenu.add_command(label="File Properties",command= commandfunc)
filemenu.add_command(label="Exit",command=root.destroy)


editmenu = Menu(mymenu,tearoff=0)
mymenu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command= commandfunc)
editmenu.add_command(label="Copy",command= commandfunc)

pastemenu = Menu(editmenu,tearoff=0)
editmenu.add_cascade(label="Paste",menu=pastemenu)
pastemenu.add_command(label="Paste Special",command= commandfunc)
pastemenu.add_command(label="Paste History",command= commandfunc)

viewmenu = Menu(mymenu,tearoff=0)
mymenu.add_cascade(label="View",menu=viewmenu)
viewmenu.add_command(label="Tool Window")
viewmenu.add_command(label="Type Info")
viewmenu.add_command(label="Parameter Info")

codemenu = Menu(mymenu,tearoff=0)
mymenu.add_cascade(label="Code",menu=codemenu)
codemenu.add_command(label="Inspect Code")
codemenu.add_command(label="Code Clean Up")
codemenu.add_command(label="Reformat Code")



root.mainloop()