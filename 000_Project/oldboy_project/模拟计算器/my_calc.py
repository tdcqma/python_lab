import re
'''
#计算器作业参考：http://www.cnblogs.com/wupeiqi/articles/4949995.html
expression='1-2*((60+2*(-3-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

    》》 用到的正则匹配 《《
# \d+\.*\d*     -> 可匹配1位整数数字、多位整数数字、或含有小数点数字，即任何数字类型
# [\*\/]+       -> 要么匹配*号，要么匹配/号
# [\+\-]?\d+    -> 要么匹配+号，要么匹配-号，要么什么都不匹配，可对数字正负数进行匹配，如+2,-2,2
# [\+\-]{1}\d   -> 表示+号或-号必须又一个是匹配的，与后边的数字组合。类似+2，-31
# \(([\+\-\*\/]*\)  -> 表示小括号内可能有+或-或*或/或什么都没有
# \(([\+\-\*\/]*\d+)\)  -> 表示小括号内可能是-22或+22或/22或*22或22
# \(([\+\-\*\/]*\d+\.*\d*)\) -> 表示小括号内可能是-22.53或+22.53或/22.53或*22.53或22.53
# \(([\+\-\*\/]*\d+\.*\d*){2,}\)    ->表示小括号内可能是-22.53+29*23.29/99,就是两种以上的（符号+数字）的组合构成的表达式

总的思路：
    寻找发现的第一个完整的小括号后调用乘除函数或加减函数计算出结果，
    然后与前后的表达式重新拼装成一个大的表达式，在这个大的表达式里在继续寻找第一个完整的小括号调用加减乘除函数计算结果，
    依次层层递归，直到把所有小括号的括号都消灭掉。
    最后一次调用compute函数计算普通的加减乘除运算即可。
'''

def compute_mul_div(arg):
    '''
    乘法计算
    :param arg: 列表格式，例如['-3-40.0/5', 0]
    :return:不需要有最终结果返回值，直接将最新的计算结果写入到arg中，而arg参数可以在函数compute()中共享通用的。
    '''

    # -3-40.0/5
    val = arg[0]

    # 得到的是对象，<_sre.SRE_Match object; span=(1, 7), match='3-40.0'>
    # \d+\.*\d* -> 可匹配1位整数数字、多位整数数字、或含有小数点数字，即任何数字类型
    # [\*\/]+   -> 要么匹配*号，要么匹配/号
    # [\+\-]?   -> 要么匹配+号，要么匹配-号，要么什么都不匹配，可对数字正负数进行匹配，如+2,-2,2
    # 该句匹配： 一个数字（可多位、可带小数点）乘以或者除以一个数字（可多位、可带小数点）
    # 得到结果：40.0/5
    mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',val)
    # print('--->',mch.group())

    # 如果mch对象不存在了，也就是说如果没有任何乘除法表达式了，就结束乘除法运算的函数
    if not mch:
        return

    # 加上.group()得到匹配结果，也就是上一步注释中的40.0/5
    content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',val).group()
    # print('content from compute_mul_div():',content)

    # 将乘法或除法表达式左右两端格式化成float类型，再进行乘或除，由于content是40.0/5，所以value结果为8.0
    if len(content.split('*'))>1:
        n1,n2 = content.split('*')
        value = float(n1) * float(n2)
    else:
        n1,n2 = content.split('/')
        value = float(n1) / float(n2)

    # val为 -3-40.0/5，before为 -3-，after为空
    before,after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',val,1)
    # print('before from compute_mul_div():',before)
    # print('after from compute_mul_div():',after)

    # new_str得到的结果为：-3-8.0
    new_str = "%s%s%s" % (before,value,after)
    # print('new_str:',new_str)

    # 将arg[0]重新赋值，也就是说arg[0]由传参时的-3-40.0/5变成了现在的-3-8.0
    arg[0] = new_str

    # 函数递归,直到re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',val)匹配不到为止，
    # 也就是递归到没有乘法、除法表达式为止
    compute_mul_div(arg)

def compute_add_sub(arg):
    '''
    操作计算加减
    :param arg: ['-3-8.0', 0]
    :return:不需要有最终结果返回值，直接将最新的计算结果写入到arg中，而arg参数可以在函数compute()中共享通用的。
    '''
    # print('arg from compute_add_sub:',arg)


    # 表达式在拼接的过程中会产生+-,++,-+,--这四种任意符号的连接，将其替换为正常数学的逻辑符号，即如下所示：
    '''
        [before]expression from exec_bracket: 1-2*(-3817949.3809523815-(-4*3)/(16-3*2))
        [after]expression from exec_bracket: 1-2*(-3817949.3809523815--12.0/(16-3*2))
        
        以上表达式的3809523815-(-4*3)会变成3809523815--12.0，这样就产生了两个--号，负负得正即将--替换为+号。
    '''
    while True:
        if arg[0].__contains__('+-') or arg[0].__contains__('++') or arg[0].__contains__('-+') or arg[0].__contains__('--'):
            arg[0] = arg[0].replace('+-','-')
            arg[0] = arg[0].replace('++','+')
            arg[0] = arg[0].replace('-+','-')
            arg[0] = arg[0].replace('--','+')
        else:
            break

    # arg[0] 为 -3-8.0 ， 将 -3-8.0 变换为 -（3+8.0）的形式，
    # 根据arg[1]的值来决定arg[0]的值是否需要加负号，即arg[1]值为1时arg[0]前加负号
    # 具体执行判断的操作在函数compute()的divmod()中判断。
    if arg[0].startswith('-'):
        arg[1] += 1
        arg[0] = arg[0].replace('-','&')    #   &3&8.0
        # print('...1...',arg[0])
        arg[0] = arg[0].replace('+','-')    #   &3&8.0
        # print('...2...', arg[0])
        arg[0] = arg[0].replace('&','+')    #   +3+8.0
        # print('...3...', arg[0])
        arg[0] = arg[0][1:]                 #   3+8.0
        # print('...4...', arg[0])

    # val为最终的arg[0],即 3+8.0
    val = arg[0]
    # print('val from compute_add_sub:',val)

    # mch为<_sre.SRE_Match object; span=(0, 5), match='3+8.0'>
    mch = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*',val)
    # print('mch from compute_add_sub:',mch)

    # 与乘除法的匹配规则类似，此处指如果再也匹配不到加减法表达式存在就停止该函数的运行。
    if not mch:
        return

    # content: 3+8.0
    content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val).group()
    # print('content from compute_add_sub:',content)

    # 分割字符串，执行加减法允许，float计算得到的结果也是float
    if len(content.split('+')) >1:
        n1,n2 = content.split('+')
        value = float(n1) + float(n2)
    else:
        n1,n2 = content.split('-')
        value = float(n1) - float(n2)

    # before和after用于与括号里的表达式的结果拼接用，可为空
    before,after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*',val,1)
    # print('before from compute_add_sub:', before)
    # print('after from compute_add_sub:', after)

    # 到这里，已经去掉了一层括号，然后拼装成一个新的表达式赋值给arg，也就是更新了arg，然后交给compute。
    '''
        [更新前：]expression from exec_bracket: 1-2*(-3817949.3809523815-(-4*3)/(16-3*2))
        
        [更新后：]expression from exec_bracket: 1-2*(-3817949.3809523815--12.0/(16-3*2))
    '''
    new_str = "%s%s%s" % (before,value,after)
    # print('new_str from compute_add_sub:', new_str)

    arg[0] = new_str
    compute_add_sub(arg)

def compute(expression):
    '''
    操作加减乘除
    :param expression: 表达式
    :return: 计算结果
    '''

    # ['-3-40.0/5', 0]
    inp = [expression,0]

    # 处理表达式中的乘除表达式，得到结果与前后的数字组合成加减表达式，并再次赋值给参数inp
    compute_mul_div(inp)

    # 由上一步处理好了乘除表达式后，inp已变为加减表达式，此处就是处理表达式中的加减法
    compute_add_sub(inp)
    # print('inp from compute:',inp)

    # divmod(inp[1],2) #结果1/2得到除数是0，余数是1，故(0, 1)
    if divmod(inp[1],2)[1] == 1:
        result = float(inp[0])
        result = result * -1
    else:
        result = float(inp[0])

    # compute函数将运算结果的确切的数字返回到exec_bracket
    return result

def exec_bracket(expression):
    '''
    递归处理括号，并计算
    :param expression:表达式参数
    :return: 最终计算结果
    '''

    # 如果表达式中已经没有带括号的表达式时，则直接调用负责计算的函数得到结果并返回，如最后是2*1-82+444的话，就直接调用compute()函数进行计算
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',expression):
        final = compute(expression)
        return final

    # >> (-3-40.0/5)
    # 正则匹配可以理解为【符号(+-*/)与数字(含小数)】的一个单独的组合，类似匹配到了-3与-40.0与/5三个单独的组。
    # 后边的{2,}代表至少有两组，因为至少有2组才是一个表达式,当然也可以有多个组合，类似(-3-40.0/5+3*2)
    # 再加上开头和结尾的\(与\)就代表匹配第一个完整的带括号的表达式了。第一个匹配到的结果是(-3-40.0/5)
    content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',expression).group()
    # print('content:',content,'type:',type(content))

    before,nothing,after = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',expression,1)
    print('[before]expression from exec_bracket:', expression)
    # print(before,'<>-----<>',after)

    # -3-40.0/5
    content = content[1:len(content)-1] #
    # print('content:',content,'type:',type(content))

    # 计算，提取的表示（-40.0/5）,并获得结果，即-40/5=-8.0，每次调用都会去掉一层小括号
    # exec_bracket收到值ret后继续拼接成一个新的含有其他小括号的表达式。
    ret = compute(content)
    # print('ret from exec_bracket:',ret)
    # print("%s=%s" % (content,ret))

    # 到此为止，已经可以完整计算出一个括号内到所有运算表达式并得到结果
    # 接下来将执行结果进行拼接,"1-2*((60+2*(-3-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"

    expression = "%s%s%s" % (before,ret,after)
    print('[after]expression from exec_bracket:',expression)

    print("="*10,'上一次计算结果',"="*10)

    return exec_bracket(expression)

if __name__ == '__main__':
    inpp = "1-2*( (60+2* (-3-40.0/5) * (9-2*5/3+7/3*99/4*2998+10*568/14)) - (-4*3) / (16-3*2) )"
    # inpp = "1-2*-30/-12*(-20+200*-3/-200*-300-100)"
    inpp = re.sub('\s*','',inpp)    # 将任意空白字符(\n\t\r\f)去除
    print('inpp:',inpp)
    result = exec_bracket(inpp)
    print('\n标准答案：',eval(inpp))
    print('运行结果：',result)