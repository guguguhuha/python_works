from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("我的第一个GUI窗口")
root.geometry("500x300+400+200")
bto_1 = Button(root)
bto_1['text'] = "送你一朵小红花"
bto_1.pack()


def songhua(e):
    messagebox.showinfo("Message",'送你一朵小红花！')


bto_1.bind("<Button-1>",songhua)

root.mainloop()