from tkinter import *
from tkinter import messagebox

def anniu(e):
    messagebox.showinfo("Message",'啦啦啦啦啦')
def anniu_1():
    print("lalalalalalla")
root = Tk()
root.text="try_2"
root.geometry("500x300+400+200")
bto_1=Button(root)

bto_1['text']="lalala"
bto_1.pack()
bto_1.bind("<Button-1>",anniu)
bto_2=Button(root,
             text="try",
             command = anniu_1,
             state="disable"  # 禁用按钮
             ,).pack()


root.mainloop()