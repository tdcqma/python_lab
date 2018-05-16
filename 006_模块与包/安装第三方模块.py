# 在python中，安装第三方模块，是通过包管理工具pip完成的。
# 如果你正在使用mac或linux，安装pip本身这个步骤就可以跳过了。

# 如果你在使用windows，在安装python时勾选'pip'和'Add python.exe to Path'
# 在命令提示符窗口下运行pip，如果windows提示未找到命令，可以重新运行安装程序添加pip。

# 注意：Mac或Linux上可能并存python3.x和python2.x，因此对应的命令是pip3

# 现在，安装第三方库 -- python imaging library （非常强大的处理图像工具库）

# pip install Pillow

# 耐心等待下载并安装后，就可以使用Pillow了。
# 有了Pillow，处理图片易如反掌。随便找个图片生成缩略图：

'''

>>> from PIL import Image
>>> im = Image.open('test.png')
>>> print(im.format, im.size, im.mode)
PNG (400, 300) RGB
>>> im.thumbnail((200, 100))
>>> im.save('thumb.jpg', 'JPEG')

其他常用的第三方库还有MySQL的驱动：mysql-connector-python，
用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2，等等。

'''

#《模块搜索路径》
#  当我们试图加载一个模块时，python会在指定的路径下搜索对应的.py文件，如果
# 找不到，就会报错：

'''
>>> import mymodule
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named mymodule
'''

# 默认情况下，python解释器会搜索当前目录目录、所有已安装的内置模块和第三方模块
# 搜索路径存放在sys模块的path变量中：

import sys
print(sys.path)

# 如果我们要添加自己的索索目录，有两种方法：
# 一是直接修改sys.path，添加要搜索的目录：

sys.path.append('/Users/mahaibin/PycharmProjects/python_basic/')

# 新建一个hello的模块，然后把hello.py模块放到路径：/Users/mahaibin/PycharmProjects/python_basic/
# 就可以直接导入了

import hello

# 第二种方法是设置环境变量PYTHONONPATH，该环境变量的内容会被自动加到模块的搜索路径中
# 设置方法与设置path环境变量类似。注意，你只要添加自己的搜素路径，python自己本身的索索路径不会受影响。





