import pymysql.cursors

"""

0. 参考连接：https://www.cnblogs.com/woider/p/5926744.html

1. 创建数据库
mysql> create database testdb character set utf8

2. 创建数据表
DROP TABLE IF EXISTS `trade`;

CREATE TABLE `trade` (
  `id` int(4) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(6) NOT NULL COMMENT '用户真实姓名',
  `account` varchar(11) NOT NULL COMMENT '银行储蓄账号',
  `saving` decimal(8,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '账户储蓄金额',
  `expend` decimal(8,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '账户支出总计',
  `income` decimal(8,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '账户收入总计',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `trade` VALUES (1,'乔布斯','18012345678',0.00,0.00,0.00);

"""

# 数据库连接
connect = pymysql.Connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'testdb',
    charset = 'utf8'
)

# 获取游标
cursor = connect.cursor()

# 插入数据
# sql = "INSERT INTO trade (name,account,saving) VALUE ('%s','%s',%.2f)"
# data = ('雷神4','13877777777',20000)
# cursor.execute(sql % data)
# connect.commit()
# print('成功插入',cursor.rowcount,'条数据。')

# 查询数据
# sql = "SELECT * FROM trade WHERE account = '%s'"
# data = ('13866666666')
# cursor.execute(sql % data)
#
# for row in cursor.fetchall():
#     print("Name:%s\tSaving:%.2f" % (row[1],row[3]))
# print("共查出",cursor.rowcount,"条数据。")

# 修改数据
# sql = "UPDATE trade SET saving = %.2f WHERE account = '%s'"
# data = (8888,'13866666666')
# cursor.execute(sql % data)
# connect.commit()
# print('成功修改',cursor.rowcount,'条数据。')

# 删除数据
# sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d" # LIMIT 后面指定删除几条符合筛选条件的记录
# data = ('13877777777',2)
# cursor.execute(sql % data)
# connect.commit()
# print('成功删除',cursor.rowcount,'条数据！')

# 事物处理
sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '13877777777' "
sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '13877777777' "
sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '13877777777' "

try:
    cursor.execute(sql_1)  # 储蓄增加1000
    cursor.execute(sql_2)  # 支出增加1000
    cursor.execute(sql_3)  # 收入增加2000
except Exception as e:
    connect.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    connect.commit()  # 事务提交
    print('事务处理成功', cursor.rowcount)

# 关闭连接
cursor.close()
connect.close()













