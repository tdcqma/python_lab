import pymysql.cursors
import smtplib
import datetime
from email.mime.text import MIMEText

"""
脚本目的：
    1. 创建邮件发送器
    2. 连接Mysql数据库，读取数据库中所有的漏洞信息
    3. 根据数据库读取的信息匹配严重、高危、中危、低危几个等级漏洞，
       再根据对应剩余的天数判断是否发送邮件。
"""

# 邮件发送
def sendEmail(receivers,title,content):

    # # 第三方 SMTP 服务 的配置信息
    mail_host = 'smtp.126.com'  # 设置服务器名
    mail_user = 'tdcqma@126.com'  # 用户名
    mail_pass = '123456'  # 密码,此处的密码是授权码
    sender = 'tdcqma@126.com'

    # message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式-文本, 编码
    message = MIMEText(content, 'html', 'utf-8')  # 内容, 格式-html, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


# 数据库连接
connect = pymysql.Connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'confluence_vul_warning',
    charset = 'utf8'
)

# 获取游标
cursor = connect.cursor()

#查询数据 - 查询全部
sql = "SELECT * FROM vul_process"
cursor.execute(sql)
db_list = []
for row in cursor.fetchall():
    row = list(row) # 将元祖转成列表
    # 获取建议修复日期，默认是字符串格式
    strformat_should_repair_date = row[10]

    # 将"建议修复日期"转换为日期格式
    dateformat_should_repair_date = datetime.datetime.strptime(strformat_should_repair_date,'%Y-%m-%d')

    # 获取今天的日期
    today = datetime.datetime.now()

    # 计算从当前天开始到建议修复日期前的剩余天数，用变量differ_days表示,然后转成int格式
    differ_days = dateformat_should_repair_date - today
    # 如果剩余天数小于1天，那么将differ_days 归0，否则大于1天的情况下就使用上面计算得到的值。
    if differ_days < datetime.timedelta(days=1):
        differ_days = 0
    else:
        differ_days = int(str(differ_days).split(' ')[0])


    # 开始过滤，符合条件的发邮件
    # 如果剩余修复天数为正，并且除去已修复的选项
    if differ_days > 0 and not str(row[8]).startswith('已修复'):

        # 获取收件人信息：receivers_mail
        receivers = row[4].split(',')
        # print('#####',receivers_mail,type(receivers_mail))

        # 获取漏洞标题 title
        vul_title = row[5]
        title = '[未修复安全风险通知_' + str(today.strftime("%Y-%m-%d")) + ']-' + row[5]  # 邮件主题
        # print('#####',title,type(title))

        vul_level = row[7]

        content = """
                   <p>您好</p>
                   <p>今天是[%s]日，您所负责的漏洞[%s(%s)]尚未修复，请在漏洞截止日期[%s]前完成修复(还剩余%s天)，感谢配合！</p>
                   <p>本邮件由系统发出，如果您已完成修复请忽略。</p>
                   """ % (today.strftime("%Y-%m-%d"), vul_title,vul_level, strformat_should_repair_date, differ_days)


        # 情景1：如果是中危、且剩余修复天数仅剩下7天的情况
        if row[7].startswith('中') and differ_days >= 0 and differ_days <=7:

            #  在这个期间内，单号回发送催促修复的邮件
            if differ_days % 2 != 0:
                print('今天发邮件！！！')
                sendEmail(receivers,title,content)
            else:
                print('今天不发邮件!!!')

            print(row[0],'\t',row[5],'\t',row[7],'\t',row[8],'\t',row[9],'还有几天到应该修复的那天：',differ_days,'天。')

        # 情景2:如果是高危、且剩余修复天数仅剩下3天的情况
        if row[7].startswith('高') and differ_days >= 0 and differ_days <=3:
            sendEmail(receivers,title,content)
            print(row[0], '\t', row[5], '\t', row[7], '\t', row[8], '\t', row[9], '还有几天到应该修复的那天：', differ_days, '天。')

print("共查出",cursor.rowcount,"条数据。")

# 关闭连接
cursor.close()
connect.close()













