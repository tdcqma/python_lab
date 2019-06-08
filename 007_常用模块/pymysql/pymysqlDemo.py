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
sql = "INSERT INTO trade (name,account,saving) VALUE ('%s','%s',%.2f)"
data = ('雷军','13866666666',10000)
cursor.execute(sql % data)
connect.commit()
print('成功插入',cursor.rowcount,'条数据。')


