from tkinter import *
import random

def creat():
    for i in range(10):
       x1=random.randrange(int(canvas['width'])/2)
       y1=random.randrange(int(canvas['height'])/2)
       x2=random.randrange(x1+int(canvas['width'])/2)
       y2=random.randrange(x2+int(canvas['height'])/2)
       canvas.create_rectangle(x1, y1, x2, y2)

root = Tk()
root.title("canvas")
root.geometry("500x300+400+200")

canvas = Canvas(root, width=300,height=200,bg="green")
canvas.pack()
line=canvas.create_line(10,10,30,20,40,50)
rect=canvas.create_rectangle(50,50,100,100)
circle = canvas.create_oval(50,50,100,100)
# imagefile=PhotoImage(file='time1.png')
# image=canvas.create_image(100,100,anchor='nw',image=imagefile)
Button(root,text="创建十个矩形",command=creat).pack()
Button(root, text="退出",command=lambda : exit()).pack()


root.mainloop()