#  基于Pycharm创建的虚拟环境移植问题

------

## 问题的引出

​		在昨天夜里，我突发奇想要不要把我创建的虚拟环境git上去，这样以后要是出了什么事，也不必一个一个包的再去安装，所以我就将整个`PYTHON_ENV`文件夹拷贝到了我的`GIT`文件夹下。拷贝完成之后，来随便写一个`Hello World!`来验证一下，拷贝过来的虚拟环境它还可以用吗？

​		于是便开始了一系列的工作：

1. 添加虚拟环境：

   ![image-20210616100212791](%E5%9F%BA%E4%BA%8Epycharm%E5%88%9B%E5%BB%BA%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E7%A7%BB%E6%A4%8D%E9%97%AE%E9%A2%98.assets/image-20210616100212791.png)

2. 验证是否可用：

   ![image-20210616100010448](%E5%9F%BA%E4%BA%8Epycharm%E5%88%9B%E5%BB%BA%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E7%A7%BB%E6%A4%8D%E9%97%AE%E9%A2%98.assets/image-20210616100010448.png)

   哎，我们发现复制过来的环境居然可以使用哎！这难道不是一件很开兴的事吗?

3. 问题出现：

   后来在在使用**`Terminal`**的时候发现，在这里面使用我们的`pip`命令之后，它居然是**全局**的命令，这就很不友好，要记得在没有拷贝之前，使用这些命令的作用范围都是**虚拟环境**内的，那这该怎么办呢？

-------

## 问题的发现

### 查看虚拟环境文件夹

​		出现问题之后，就逐渐开始怀疑虚拟环境所在的文件夹了，是不是里面有着相关的配置文件呢？

​		我们来看看其中的文件构造：

<img src="%E5%9F%BA%E4%BA%8Epycharm%E5%88%9B%E5%BB%BA%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E7%A7%BB%E6%A4%8D%E9%97%AE%E9%A2%98.assets/image-20210616101324767.png" alt="image-20210616101324767" style="zoom:50%;" />

其中`include`文件夹是一个空文件夹，而`pyvenv.cfg`的内容呢，是我们基于什么环境所创建的虚拟环境。

```
home = D:\Install\Python\Python372
include-system-site-packages = false
version = 3.7.2
```

​		那么，此时问题肯定就在剩余的文件夹中了，而打开`lib`文件夹发现这里面都是一些我们所安装的包的一些相关文件。此时问题便逐渐的归到了`Scripts`文件夹了，打开文件夹一看：

<img src="%E5%9F%BA%E4%BA%8Epycharm%E5%88%9B%E5%BB%BA%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E7%A7%BB%E6%A4%8D%E9%97%AE%E9%A2%98.assets/image-20210616102027032.png" alt="image-20210616102027032" style="zoom:50%;" />

那么此时，问题便可归于前四个文件了，`active`,`active.bat`,`Active.ps1`,`deactive.bat`.

### 创建一个新的虚拟环境与之比对

​		由于我们可能已经找到了引起这个问题出现的关键性文件，所以我们便可以在随便再创建一个文件与它进行比对：

1. `active`文件：

   在这个文件中我们发现了一共有两处不同：

   ![image-20210616102814793](%E5%9F%BA%E4%BA%8Epycharm%E5%88%9B%E5%BB%BA%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E7%A7%BB%E6%A4%8D%E9%97%AE%E9%A2%98.assets/image-20210616102814793.png)

   ![image-20210616103053247](%E5%9F%BA%E4%BA%8Epycharm%E5%88%9B%E5%BB%BA%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E7%A7%BB%E6%A4%8D%E9%97%AE%E9%A2%98.assets/image-20210616103053247.png)

   那么，很容易看出第一处不同是路径，它还是我拷贝之前的路径，第二处不同显然是虚拟环境的名称，现在我们将它改正过来。

2. `activate.bat`文件：![image-20210616124033258](%E5%9F%BA%E4%BA%8Epycharm%E5%88%9B%E5%BB%BA%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E7%A7%BB%E6%A4%8D%E9%97%AE%E9%A2%98.assets/image-20210616124033258.png)

   这和上面的问题都一样。

3. `Activate.ps1`文件：![image-20210616124244804](%E5%9F%BA%E4%BA%8Epycharm%E5%88%9B%E5%BB%BA%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E7%A7%BB%E6%A4%8D%E9%97%AE%E9%A2%98.assets/image-20210616124244804.png)

   同样是路径的问题。

4. `deactive.bat`文件：

![image-20210616124408034](%E5%9F%BA%E4%BA%8Epycharm%E5%88%9B%E5%BB%BA%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E7%A7%BB%E6%A4%8D%E9%97%AE%E9%A2%98.assets/image-20210616124408034.png)

​	没有差别。

### 解决方法

1. 找到你所创建的虚拟环境文件夹。

2. 打开`Scripts`文件夹。

3. 找到`active`文件，找到第40行，将`VIRTUAL_ENV=" "`双引号里改为你拷贝后的路径。

4. 找到`active.bat`文件，找到第11行，将`set "VIRTUAL_ENV=`改为你拷贝后的路径。

5. 找到`Active.ps1`文件，找到第30行，将`$env:VIRTUAL_ENV=" "`双引号里改为你拷贝后的路径。

6. 在这里有两种方法：

   1. 如果你的`pip`版本不是最新的，你可以采用如下方式：

      在全局环境下激活我们的虚拟环境

      运用 `python -m pip install --upgrade pip`命令
   
      ```python
      # 示例
      # 打开命令行输入如下代码
      D:\Data\GIT\python_Practice\PYTHON_ENV\DIGIFAX_ENV\Scripts\activate.bat # 这里的路径是你虚拟环境下的路径
      python -m pip install --upgrade pip
      ```

      

   2. 进入虚拟环境下，删除`Scripts`文件夹下的![image-20210616145022911](%E5%9F%BA%E4%BA%8Epycharm%E5%88%9B%E5%BB%BA%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E7%A7%BB%E6%A4%8D%E9%97%AE%E9%A2%98.assets/image-20210616145022911.png)

      接着删除`Lib\site-packages`下![image-20210616164943123](%E5%9F%BA%E4%BA%8Epycharm%E5%88%9B%E5%BB%BA%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E7%A7%BB%E6%A4%8D%E9%97%AE%E9%A2%98.assets/image-20210616164943123.png)
   
      然后进入`Pycharm`的环境配置界面,会看见有黄色高亮的这一行，点击`Insatll packaging tools`便可。![image-20210616145353486](%E5%9F%BA%E4%BA%8Epycharm%E5%88%9B%E5%BB%BA%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E7%A7%BB%E6%A4%8D%E9%97%AE%E9%A2%98.assets/image-20210616145353486.png)
   
      然后静待片刻，就会发现和以前一样可以使用了，**如若不行再来一次！**
   
   
   
   ​		当然了，你要是觉得此种方法有点麻烦，你可以在`pycharm`中指定一个旧版本的`pip`进行安装，再将其更新，采用第一种方法。



