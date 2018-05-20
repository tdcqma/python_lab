import xml.etree.ElementTree as ET

# 指定解析目标文件，将对象保存到tree
tree = ET.parse("a.xml")

# 从对象中获取根节点，即data
root = tree.getroot()

# 打印每个节点的三个属性：tag、attrib、text
# print(root.tag)
# print(root.attrib)
# print(root.text)
'''
data
{}
'''

# 从整个树形结构中查找
# res = root.iter('year')
# print(res)
# print(list(res))
'''
<_elementtree._element_iterator object at 0x104668728>
[<Element 'year' at 0x10465d2c8>, <Element 'year' at 0x104666b38>, <Element 'year' at 0x104666cc8>]
'''

# res = root.iter('year')
# for item in res:
#     print(item.tag,item.attrib,item.text)
'''
year {} 2008
year {} 2011
year {} 2011
'''

# 从当前节点的儿子中查找
# res = root.find('year')
# print(res)
# => None

# 从当前节点的儿子中查找,找成功 一个就结束
# res=root.find('country')
# print(res.attrib)

# 从当前节点的儿子中找到第一个country，然后在第一个conuntry中继续找第一个year
# res=root.find('country').find('year')
# print(res.text)

# 从当前节点的儿子中查找,找到所有，类似于iter()
# res_iter = root.iter('country')
# res_findall=root.findall('country')
# print(res_findall)
# print(list(res_iter))
'''
[<Element 'country' at 0x1040339f8>, <Element 'country' at 0x104668a98>, <Element 'country' at 0x104668c28>]
[<Element 'country' at 0x1040339f8>, <Element 'country' at 0x104668a98>, <Element 'country' at 0x104668c28>]
'''

#【查】遍历所有xml 文件内容
# for country in root:
#     print('==============>',country.tag,country.attrib)
#     for item in country:
#         print(item.tag,item.attrib,item.text)

#【增】增加一条xml文件的记录
for country in root.findall('country'):
    for year in country.findall('year'):

        if int(year.text) > 2000:
            year2=ET.Element('year2')
            year2.text='新年'
            year2.attrib={'update':'yes'}
            country.append(year2) #往country节点下添加子节点

tree.write('a.xml.swap')
