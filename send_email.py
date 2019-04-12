# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(title, content):
	from_addr = '18838939163@163.com' # 发件人邮箱
	password = 'sbm201111' # 这里是授权码，并非邮箱密码
	smtp_server = 'smtp.163.com' # smtp 服务器地址
	
	to_addr = '1351718272@qq.com' # 收件人邮箱
	

	msg = MIMEText(content, 'plain', 'utf-8')
	msg['From'] = '{}'.format(from_addr)
	msg['To'] = to_addr
	msg['Subject'] = title

	server = smtplib.SMTP_SSL(smtp_server, 465) # SSL端口465
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()

if __name__ == '__main__':
	send_email('hello man','give me something.')	