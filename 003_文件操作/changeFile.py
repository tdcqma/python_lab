# 要求将src.txt中的第一行“李杰”后面加入“[年龄是73岁]”,思路是将硬盘指针指向第六个字节，然后从第7个字节处开始写。
# 以下是错误的示例，即使用seek方法将硬盘指针跳过“李杰”两个字符，也就是6个字节。从第7个字节开始写入，也就是在李杰的后面了。
# 但是这样有一个问题，就是写入的内容其实是覆盖了后边的内容的，所以这种做法不可取。

#with open(r'src.txt',mode='rt+',encoding='utf-8') as f:
#	f.seek(6)
#	f.write('[年龄是73岁]')


# 【1】修改文件内容的方式1:
# 思路为先把内容所有都读出来，对想要修改的部分进行修改后保存在一个data的变量中，
# 此时这个变量是保存在内存中的，状态为字符串类型。同时再打开一个相同的文件，
# 将刚刚保存在内存中的变量在写回去。
# 这种方式的弊端是一次读取文件全部的内容到内存中，机器容易卡死。

#with open(r'src.txt',mode='r',encoding='utf-8') as f:
#	data = f.read()
#	data = data.replace('武佩奇','wxx')
#with open(r'src.txt',mode='w',encoding='utf-8') as f_write:
#	f_write.write(data)


#【2】修改文件内容的方式2:先读取原始文件，再读区一个交换临时文件（src.txt.swap）,for循环原始文件得到line，然后判断line中是否存在wxx，如果存在把line中的wxx替换为五大郎，然后再次赋值给line，最后在判断语句if外把所有的line都写入新的src.txt.swap文件中。
import os

with open(r'src.txt',mode='r',encoding='utf-8') as f,open(r'src.txt.swap',mode='w',encoding='utf-8') as f_new:
	for line in f:
		if 'wxx' in line:
			line = line.replace('wxx','武大郎')
			#line = line.strip('\n')
		f_new.write(line)

# 这个时候其实源文件并没有改变，只是增加了一个更改内容后的新文件了。我们要做的就是，删除旧文件然后把新文件改成源文件名即可。
# 这个操作需要倒入os模块

os.remove('src.txt')
os.rename('src.txt.swap','src.txt')
