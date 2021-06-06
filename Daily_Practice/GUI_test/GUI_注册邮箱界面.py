import tkinter


def calc():
    # (1)此处从Entry控件的实例t1取值，为id变量赋值
    id = t1.get()
    sel = v.get()
    tn = ['学生', '教师', '校友']
    p = ['stu.', '', 'alu.']
    # (2)此处格式化生成邮箱地址字符串赋值给变量s
    s = t1.get()+"@"+p[int(sel)]+'xxu.edu.cn'
    lb3.config(text = s)


root = tkinter.Tk()
root.title('邮箱注册')
tkinter.Label(root, text="请选择身份：").pack()
v = tkinter.IntVar()

rd1 = tkinter.Radiobutton(root, text="学生", variable=v, value=0)
rd1.pack()
# (3)此处设置第2个单选按钮，文本为“教师”,返回值为1
rd2 = tkinter.Radiobutton(root, text="教师", variable=v, value=1)
rd2.pack()

rd3 = tkinter.Radiobutton(root, text="校友", variable=v, value=2)
rd3.pack()
tkinter.Label(root, text="请输ID号").pack()
t1 = tkinter.Entry(root)
# (4)此处将Entry控件的实例t1放置在窗体上
t1.pack()
bt = tkinter.Button(root, text='注册', command=calc)
bt.pack()
lb3 = tkinter.Label(root, text='结果记录')
lb3.pack()

root.mainloop()

