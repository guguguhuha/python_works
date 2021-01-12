from tkinter import *
from tkinter import messagebox


def login():
    username=v1.get()
    password = v2.get()
    print("去数据库比对用户名和密码")
    print("用户名: " + v1.get())
    print("密码: " + v2.get())
    if username=='qwer' and password == '1234':
        messagebox.showinfo("Message","欢迎！")
    else:
        messagebox.showinfo("Message","登录失败\n用户名或密码错误！")


root = Tk()
root.title("entry")
root.geometry("500x300+400+200")

lable_1=Label(root,text="用户名").pack(fill=X)

v1=StringVar()
entry_1=Entry(root,textvariable=v1).pack()
#v1.set("aaaasad")#给一个默认的值

lable_2=Label(root,text="密码").pack(fill=X)

v2=StringVar()
entry_2=Entry(root,textvariable=v2,show="*").pack()

button_1=Button(root, text='登录',command=login).pack()


root.mainloop()