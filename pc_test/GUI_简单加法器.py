from tkinter import *

def SUM():
    a=float(_1.get())
    b=float(_2.get())
    s="%.2f+%.2f=%.2f\n"%(a,b,a+b)
    txt.insert(END, s)
def DEL():
    _1.delete(0,END)
    _2.delete(0,END)
    txt.delete(0.0,END)
root=Tk()
root.title("简单加法器")
root.geometry("500x300+400+200")

L_1=Label(root,text="请分别输入一个数，在下面的方框里").pack()
_1=Entry(root,bg="gray",);_1.place(relx=0.1,rely=0.1)
_2=Entry(root,bg="gray",);_2.place(relx=0.6,rely=0.1)
txt=Text(root,width=40,height=10,bg="gray");txt.place(rely=0.5,relx=0.2,x=10)

b_1=Button(root, text="加法",command=SUM)
b_2=Button(root, text="清除",command=DEL)
b_1.place(relx=0.1,rely=0.3,relwidth=0.3);b_2.place(relx=0.6,rely=0.3,relwidth=0.3)

root.mainloop()

