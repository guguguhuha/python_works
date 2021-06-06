from tkinter import *

def com(j):
    c=''
    c+=str(j)
    v.set(c)


root = Tk()
root.title("计算器布局 ")
root.geometry("143x231")

btntext=(("MC","M+","M-","MR"),
         ("C","±","÷","×"),
         (7,8,9,"-"),
         (4,5,6,"+"),
         (1,2,3,"="),
         (0,"."))

v=StringVar()
Entry(root,textvariable=v).grid(row=0, column=0, sticky=EW,columnspan=4,pady=15)



for iindex,i in enumerate(btntext):
    for jindex,j in enumerate(i):
        if j == 0:
            Button(root, text=j,)\
                .grid(row=iindex + 1, column=jindex, sticky=EW,columnspan=2)
        elif j == "=":
            Button(root, text=j,)\
                .grid(row=iindex + 1, column=jindex, sticky=NSEW,rowspan=2)
        elif j == ".":
            Button(root, text=j,)\
                .grid(row=iindex + 1, column=jindex+1, sticky=EW)
        else:
            Button(root,text=j,)\
                .grid(row=iindex+1,column=jindex,sticky=EW)


root.mainloop()