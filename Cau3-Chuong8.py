from tkinter import *
from tkinter import messagebox


top=Tk()
v = IntVar()

def clickhere():
    messagebox.showinfo("Click me","Em Chào Thầy")

button=Button(top,text="Click me",command=clickhere)
button.place(x=62,y=1)


Radiobutton(top, text="First", variable=v, value=1).pack(anchor=W)
Radiobutton(top, text="Second", variable=v, value=2).pack(anchor=W)
Radiobutton(top, text="Third", variable=v, value=3).pack(anchor=W)
mainloop()



