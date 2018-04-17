# 实现效果：python3 copy.py src_file_path dst_file_path 即可实现文件的复制

import sys,os

# sys.argv可以拿到脚本执行时传来的参数，并保存在列表里。索引为0的位置为脚本本身，从索引为1的位置开始就是参数了。
# 例如：以下代码中copy.py为执行脚本，后边所有的均为参数。
#$ python3 copy.py src_file_path dst_file_path aa bb cc
#['copy.py', 'src_file_path', 'dst_file_path', 'aa', 'bb', 'cc']

#print(sys.argv)


src_file_path = sys.argv[1]
if not os.path.isfile(src_file_path):
	print('文件不存在')
	sys.exit()	# 写脚本的时候，可以使用sys.exit(),退出整个脚本，干掉整个程序
dst_file_path = sys.argv[2]

with open(r'%s' % src_file_path,mode='rb') as read_f,open (r'%s' % dst_file_path,mode='wb') as write_f:
	for line in read_f:
		write_f.write(line)
	
