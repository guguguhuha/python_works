from tkinter import *

def _1():
    txt.insert(INSERT,"hello")
    txt.insert(END,"end")
def _2():
    print("所有内容 ："+txt.get(1.0,END))
def _3():
    pass
def _4():
    pass
def _5():
    txt.delete(1.0,END)
    txt.insert(1.0,"work work hard \nday day up !")

root = Tk()
root.title("text")
root.geometry('500x300+400+200')

txt=Text(root,width=40,height=12,bg="gray")
txt.pack()
txt.insert(1.1,"12345\n66789")
txt.insert(2.0,"咕咕咕呼哈，啦啦啦乌拉，咻咻咻嘿咻")

Button(root,text='插入文本',command=_1).pack(side=LEFT)
Button(root,text='返回文本',command=_2).pack(side=LEFT)
Button(root,text='插入图片',command=_3).pack(side=LEFT)
Button(root,text='添加组件',command=_4).pack(side=LEFT)
Button(root,text='通过tag精确控制文本',command=_5).pack(side=LEFT)
Button(root,text='退出',command=lambda : quit()).pack(side=LEFT)

root.mainloop()