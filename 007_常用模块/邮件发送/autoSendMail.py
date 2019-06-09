import smtplib

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

# 计划任务 创建后台执行的schedulers
sched = BlockingScheduler()

from email.mime.text import MIMEText

# # 第三方 SMTP 服务
mail_host = 'smtp.126.com' # 设置服务器名
mail_user = 'tdcqma@126.com' # 用户名
mail_pass = '123456' # 密码,此处的密码是授权码

sender = 'tdcqma@126.com'
receivers = ['tdcqma@163.com','mahaibin@imdada.cn'] # 指定多个收件人


content = """
<p>您好</p>
<p>您所负责的漏洞*****尚未完成修复，请在漏洞截止日期****前完成修复，感谢配合！</p>
<p>本邮件由系统发出，如果您已完成修复请忽略。</p>
"""

today = str(datetime.datetime.now().strftime("%Y-%m-%d"))
title = '[安全通知]_' + today # 邮件主题
def sendEmail():

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

if __name__ == '__main__':
    # sendEmail()

    # sched.add_job(sendEmail, trigger='date', run_date='2019-06-09 18:08:00')
    sched.add_job(sendEmail, trigger='date')
    sched.start()
