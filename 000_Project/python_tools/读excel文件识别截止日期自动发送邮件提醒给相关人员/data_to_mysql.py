import pymysql
import xlrd,xlwt
import datetime

"""
脚本目的：
    1. 识别Confluence_vul.xlsx中漏洞开始日期，并依据严重、高危、中危、低危对应不同修复天数的规则
       自动生成不同的应修复日期,然后生成写入到新的new_Confluence_vul.xls表格中
    2. 将新生成的new_Confluence_vul.xls表格数据写入到MySQL数据库
    
参考：
    1. https://www.cnblogs.com/fuqia/p/8989712.html
    2. https://www.cnblogs.com/tiantianhappy/p/9145260.html
    3. https://blog.csdn.net/joey_2018_/article/details/80671114
    4. https://www.cnblogs.com/baxianhua/p/8808136.html
    5. https://blog.csdn.net/lilongsy/article/details/80242427
    6. https://www.runoob.com/python3/python3-date-time.html
    7. https://www.cnblogs.com/zhengyionline/p/10397099.html
"""

data_list = []

# 读取excel表格中的数据，将所有的值前后加各上一个单引号'，然后以每一行为一个元素，添加到新的列表data_list中。
def data_receive_from_excel(path):
    worksheet = xlrd.open_workbook(path)  # 打开excel文件
    # worksheet = xlrd.open_workbook('auto_warning.xlsx')  # 打开excel文件
    sheet_names = worksheet.sheet_names()  # 获取所有的sheet，表存在列表中

    sheet_all_by_name = worksheet.sheet_by_name('all')  # 根据sheet名在打开相应的sheet

    """
    插入数据格式：
    colum_value = "values(2,'http://tdcqma.com','法律合规部','黄飞鸿','111111@163.com','跨站点脚本攻击','应用类','中危','延迟修复中','2019-06-09','2019-06-13','','漏洞扫描','www.baidu.com','测试添加记录')"

    '3.0','101.932.37.832:4200','人事行政部','王宝强','111111@163.com','Redis服务器缺乏密码认证保护','主机类','中危','延期修复中','20190506.0','','','漏洞扫描','',''
    '1.0','http://tdcqma.com','数据研发部','张三丰','111111@qq.com','目标服务器启用了OPTIONS方法','应用类','中危','修复中','20190423.0','','','漏洞扫描','','',
    """

    cols = sheet_all_by_name.ncols  # 获取excel 表中有多少列
    # print('Excel表格列数：', cols, '列')

    rows = sheet_all_by_name.nrows  # 获取excel表中有多少行记录
    # print('Excel表格行数：', rows, '行')

    for i in range(1, rows):    # 从1开始是为了略过第一行的字段名称行
        colum_value = ""
        data = sheet_all_by_name.row_values(i)
        for j in data:
            j = "'" + str(j) + "',"
            colum_value += j
        colum_value = colum_value.strip(',')
        data_list.append(colum_value)
    return data_list

# 将列表data_list中的数据写入数据库。
def data_to_mysql(data_list):

    # Mysql数据库链接,创建数据库confluence_vul_warning
    db = pymysql.connect(host='localhost',user='root',password='123456',db='confluence_vul_warning',port=3306)

    #设置游标，靠它进行数据库操作
    cursor = db.cursor()

    colum_name = "(id,app_or_host,department,master,mail_address,vul_title,vul_type,vul_level,vul_status,vul_start_date,should_repair_date,actual_repair_date,vul_from,vul_jira,vul_comment)"
    # colum_value = "values(2,'http://tdcqma.com','法律合规部','黄飞鸿','tdcqma@163.com','跨站点脚本攻击','应用类','中危','延迟修复中','2019-06-09','2019-06-13','','漏洞扫描','www.baidu.com','测试添加记录')"

    for colum_value in data_list:
        colum_value = "values(" + colum_value + ")"
        # colum_value = "values('3.0','101.93.7.83:4200','人事行政部','王宝强','tdcqma@163.com','Redis服务器缺乏密码认证保护','主机类','中危','延期修复中','20190506.0','','','漏洞扫描','','')"
        sql_insert_data = "insert into vul_process" + colum_name + colum_value
        cursor.execute(sql_insert_data)
        db.commit()
    db.close()

# 根据严重、高危、中危、低危计算每一个漏洞对应的应该修复日期，并生成新的excel表格。
def should_repair_date_counter(path):
    '''
    读取指定目录的excel，读出数据到python，然后对日期根据规则自动延长，最后写回excel
    :return: excel格式文本
    '''

    worksheet = xlrd.open_workbook('Confluence_vul.xlsx')  # 打开excel文件
    # worksheet = xlrd.open_workbook('auto_warning.xlsx')  # 打开excel文件
    sheet_names = worksheet.sheet_names()  # 获取所有的sheet，表存在列表中

    sheet_all_by_name = worksheet.sheet_by_name('all')  # 根据sheet名在打开相应的sheet

    """
    插入数据格式：
    colum_value = "values(2,'http://tdcqma.com','法律合规部','黄飞鸿','tdcqma@163.com','跨站点脚本攻击','应用类','中危','延迟修复中','2019-06-09','2019-06-13','','漏洞扫描','www.baidu.com','测试添加记录')"

    '3.0','101.93.7.83:4200','人事行政部','王宝强','1111111@163.com','Redis服务器缺乏密码认证保护','主机类','中危','延期修复中','20190506.0','','','漏洞扫描','',''
    '1.0','http://tdcqma.com','数据研发部','张三丰','1111111@qq.com','目标服务器启用了OPTIONS方法','应用类','中危','修复中','20190423.0','','','漏洞扫描','','',
    """

    cols = sheet_all_by_name.ncols  # 获取excel 表中有多少列
    # print('Excel表格列数：', cols, '列')

    rows = sheet_all_by_name.nrows  # 获取excel表中有多少行记录
    # print('Excel表格行数：', rows, '行')

    # 新excel格式设定
    def set_style(name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name
        font.bold = bold
        font.color_index = 4
        font.height = height

        style.font = font
        return style

    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet('all')

    # row0 = [u'字段名称', u'大致时段', 'CRNTI', 'CELL-ID']
    # row1 = [u'测试1', '15:50:33-15:52:14', 22706, 4190202]
    #
    # for i in range(len(row0)):
    #     data_sheet.write(0, i, row0[i], set_style('Times New Roman', 220, True))
    #     data_sheet.write(1, i, row1[i], set_style('Times New Roman', 220, True))

    # 保存文件
    # workbook.save('demo.xls')
    # workbook.save(path)
    # add_days = 0
    for row in range(0, rows):
        colum_value = ""
        data = sheet_all_by_name.row_values(row)

        for col in range(0,cols):

            if col == 9 and str(data[col]).startswith('201'):
                '''
                    add_days 代表自动计算添加的天数
                        严重-》1天
                        高危-》3天
                        中危-》14天
                        低危-》30天   
                '''
                add_days = 0
                if str(data[col-2]).startswith('严'):
                    add_days = 1
                elif str(data[col-2]).startswith('高'):
                    add_days = 3
                elif str(data[col-2]).startswith('中'):
                    add_days = 14
                elif str(data[col-2]).startswith('低'):
                    add_days = 30

                '''
                    调用time_process函数，将当前excel记录中的第9列的日期时间与上面计算得来的add_days一同传入该函数中
                    即可计算出应该修复的日期。
                    应该修复的日期用data[col+1]表示。
                '''
                data[col+1] = time_process(str(data[col]),add_days)


            '''
            经过上面的应修复日期的计算，现在已经将每一行的"建议解决日期"都以计算出，并保存在data[col]中了，
            逐一写入到新的excel中即可。
            '''
            data_sheet.write(row,col,data[col])
            # print(row,'----',col,'----',str(data[col]),'>',type(str(data[col])))

    # 保存文件
    # workbook.save('demo.xls')
    workbook.save(path)

# 日期计算器函数
def time_process(start_day,add_days):
    '''
    高中低风险修复日期不一致，因此应该修复日期计算方式为：
        根据开始日期+不同的修复日期 = 应该修复日期

    :param start_day: 漏洞开始时间
    :param add_days: 应该修复时间是几天，这个add_days代表几天。
    :return:
    '''
    # print(datetime.datetime.now())    # 获取当前时间
    # print((datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d"))    # 当前时间+7天

    # 读取字符串格式的start_day日期，然后通过datetime.datetime.strptime()转换成datetime的日期格式，
    # 以方便与datetime.timedelta(days=add_days) 相加减。
    new_start_day = datetime.datetime.strptime(start_day,'%Y-%m-%d')

    # print(type(new_start_day))    #类型是 <class 'datetime.datetime'>
    # print(new_start_day.strftime("%Y-%m-%d")) # 格式化到2019-05-02的形式

    should_repair_date = (new_start_day + datetime.timedelta(days=add_days)).strftime("%Y-%m-%d")
    return should_repair_date

if __name__ == '__main__':
    # 设置路径
    path = 'new_Confluence_vul.xls'

    # 根据严重、高危、中危、低危计算每一个漏洞对应的应该修复日期，并生成新的excel表格。
    should_repair_date_counter(path)
    print('创建'+path+'文件成功！')

    # 读取excel表格中的数据，将所有的值前后加各上一个单引号'，然后以每一行为一个元素，添加到新的列表data_list中。
    data_list = data_receive_from_excel(path)

    # 将列表data_list中的数据写入数据库。
    data_to_mysql(data_list)
    print("带有\'建议修复日期\'的新表已入库成功！")
