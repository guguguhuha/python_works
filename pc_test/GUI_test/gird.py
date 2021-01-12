from tkinter import *
from tkinter import messagebox

def login():
    username=entry_1.get()
    password = entry_2.get()
    print("去数据库比对用户名和密码")
    print("用户名: " + entry_1.get())
    print("密码: " + entry_2.get())
    if username=='qwer' and password == '1234':
        messagebox.showinfo("Message","欢迎！")
    else:
        messagebox.showinfo("Message","登录失败\n用户名或密码错误！")


root = Tk()
root.title("gird")
root.geometry("500x300+400+200")

lable_1=Label(root,text='用户名');lable_1.grid(row=0, column=0)
entry_1=Entry(root);entry_1.grid(row=0, column=1)
lable_2=Label(root,text='用户名为手机号');lable_2.grid(row=0, column=2)
lable_3=Label(root,text='密码');lable_3.grid(row=1, column=0)
entry_2=Entry(root,show="*");entry_2.grid(row=1, column=1)

Button(root,text="登录",command=login).grid(row=2,column=1,sticky=EW)
Button(root,text="取消").grid(row=2,column=2,sticky=E)

root.mainloop()