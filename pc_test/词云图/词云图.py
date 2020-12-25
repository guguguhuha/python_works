import jieba
import wordcloud
f = open("2017政府工作报告.txt", "r")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path = "msyh.ttc",
                        width = 1000,
                        height = 700,
                        background_color = "white",
                        max_words=30)
w.generate(txt)
w.to_file("grwordcloud.png")
