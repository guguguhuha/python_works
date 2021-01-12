from tkinter import *
from tkinter import messagebox

def _1():
    messagebox.showinfo("测试","你的选择是："+v.get())
root = Tk()
root.title("check_button")
root.geometry("500x300+400+200")

v=StringVar()
v.set(3)

button1=Radiobutton(root, text="boy",value="1",variable=v).pack(side=LEFT)
button2=Radiobutton(root, text="girl",value="2",variable=v).pack(side=LEFT)
button3=Radiobutton(root, text="null",value="3",variable=v).pack(side=LEFT)

Button(root,text="确定",command=_1).pack(side=LEFT)

root.mainloop()
