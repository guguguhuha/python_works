from tkinter import *


root = Tk()
root.title = "try"
root.geometry("500x300+400+200")
label_1 = Label(root,
              text = "first",
              bg ="black",
              fg ="white",
              width =10,
              height =2)
label_1.pack(fill=X)
label_2 = Label(root,
              text = "Second",
              bg ="white",
              fg ="black",
              width =10,
              height =2,
              font = ("黑体",30))
label_2.pack()
label_3 = Label(root,
               text = "听说这里有个人再学习GUI\n哈哈哈哈哈\n咕咕咕呼哈\n祝你好运",
               borderwidth=1, # 这个参数是设置框边的粗细
                relief="solid",
                justify='center')
label_3.pack()

root.mainloop()