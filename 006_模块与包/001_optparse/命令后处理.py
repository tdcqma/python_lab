from optparse import OptionParser

# 创建OptionParser对象,括号内填写usage变量时则会将在-h帮助信息的首行显示usage的内容值。
usage = "this is the method of the script."
parser = OptionParser(usage)

# 在帮助信息里会显示：-f FILENAME  write report to file.
parser.add_option("-f",dest="filename",help="write report to file.")


(options,args) = parser.parse_args()
print(options,args)
# print(options.filename)