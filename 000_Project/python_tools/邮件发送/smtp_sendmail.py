import smtplib
import datetime

from email.mime.text import MIMEText
from email.header import Header

# # 第三方 SMTP 服务
mail_host = 'smtp.126.com' # 设置服务器名
mail_user = 'tdcqma@126.com' # 用户名
mail_pass = '123456' # 密码,此处的密码是授权码

sender = 'tdcqma@126.com'
receivers = ['world@163.com','hello@hello.cn'] # 指定多个收件人

# content = '我用Python'
content = """
<p>Python 邮件发送测试...</p>
"""

today = str(datetime.datetime.now().strftime("%Y-%m-%d"))
print(today)
title = '[安全通知]_' + today # 邮件主题
print(title)
def sendEmail():

    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式-文本, 编码
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

if __name__ == '__main__':
    sendEmail()
