import xlrd

# 保存格式化后的excel行记录
data_list = []

def data_receive():
    worksheet = xlrd.open_workbook('auto_warning.xlsx') # 打开excel文件
    sheet_names = worksheet.sheet_names()    # 获取所有的sheet，表存在列表中

    sheet_all_by_name = worksheet.sheet_by_name('all') # 根据sheet名在打开相应的sheet

    """
    colum_value = "values(2,'http://tdcqma.com','法律合规部','黄飞鸿','tdcqma@163.com','跨站点脚本攻击','应用类','中危','延迟修复中','2019-06-09','2019-06-13','','漏洞扫描','www.baidu.com','测试添加记录')"
    
    '3.0','101.93.7.83:4200','人事行政部','王宝强','tdcqma@163.com','Redis服务器缺乏密码认证保护','主机类','中危','延期修复中','20190506.0','','','漏洞扫描','',''
    '1.0','http://tdcqma.com','数据研发部','张三丰','363245361@qq.com','目标服务器启用了OPTIONS方法','应用类','中危','修复中','20190423.0','','','漏洞扫描','','',
    
    """



    cols = sheet_all_by_name.ncols  # 获取excel 表中有多少列
    print('Excel表格列数：',cols,'列')

    rows = sheet_all_by_name.nrows # 获取excel表中有多少行记录
    print('Excel表格行数：',rows,'行')


    for i in range(1,rows):
        colum_value = ""
        data = sheet_all_by_name.row_values(i)
        for j in data:
            j = "'" + str(j) + "',"
            colum_value += j
        colum_value = colum_value.strip(',')
        data_list.append(colum_value)

    return data_list



    # sheet_all_by_index = worksheet.sheet_by_index(1)  # 根据sheet排列的位置选择sheet
    # print(sheet_all_by_index.row_values(1))

    # rows = sheet_all_by_name.row_values(1)    # 指定输出第几行数据，下面是获取第一行的数据
    # print(rows)

    # 获取具体单元格的数据,其中2、4代表要读取的excel表中的行号和列号
    # data = sheet_all_by_name.cell(2,4).value
    # print(data)