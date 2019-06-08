import xlwt


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()   # 初始化样式
    font = xlwt.Font()       # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height

    style.font = font
    return style


def write_excel(path):
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet('demo')
    row0 = [u'字段名称', u'大致时段', 'CRNTI', 'CELL-ID']
    row1 = [u'测试', '15:50:33-15:52:14', 22706, 4190202]
    # 生成第一行和第二行
    for i in range(len(row0)):
        print('i:',i)
        data_sheet.write(0, i, row0[i], set_style('Times New Roman', 220, True))
        data_sheet.write(1, i, row1[i], set_style('Times New Roman', 220, True))

    # 保存文件
    # workbook.save('demo.xls')
    workbook.save(path)


if __name__ == '__main__':
    # 设置路径
    path = 'Confluence_vul_1.xls'
    write_excel(path)
    print(u'创建Confluence_vul_1.xls文件成功')