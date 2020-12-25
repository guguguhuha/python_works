#文本字符分析
#统计输入的字符串，按字符出现频率并按照降序方式打印字母
text = input("请输入一段文本（回车退出)：")
while text != '':#如果为空则退出循环
    d = {}
    for word in text:
        d[word] = d.get(word,0) + 1
        # d[word]=text.count(word)
        #转为列表类型对其排序
    ls = list(d.items())
    ls.sort(key=lambda x:x[1],reverse = True)#以记录第二列排序
    for i in range(len(ls)):
        word, count = ls[i]
        print("{0:<10}{1:>5}".format(word,count))
    text = input("请输入一段文本（回车退出)：")