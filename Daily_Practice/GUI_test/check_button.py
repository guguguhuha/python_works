from tkinter import *
from tkinter import messagebox

def comfirm():
    if code.get()==1:
        messagebox.showinfo("code","hahahaha")
    if hobby.get()==1:
        messagebox.showinfo("hobby","lalalalala")


root=Tk()
root.title("check_button")
root.geometry("500x300+400+200")

code=IntVar()
hobby=IntVar()
hobby.get()

button_1=Checkbutton(root,text="code",variable=code,onvalue=1,offvalue=0,)
button_2=Checkbutton(root,text="hobby",variable=hobby,onvalue=1,offvalue=0,)
button_1.pack(side=LEFT);button_2.pack(side=LEFT)

Button(root, text="确认",command=comfirm).pack(side=LEFT)

root.mainloop()