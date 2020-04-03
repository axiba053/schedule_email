#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author      : liuqiang
@contact     : 654464405@qq.com
@Date        : 2019/12/20 
@Description :定时发邮件
'''

import smtplib
from email.mime.text import MIMEText
import schedule,time


def SendEmail(info,subject='提醒邮件',emailAccepter='654464405@qq.com',email_pwd='******'):
    email_host = 'smtp.126.com'     #邮箱服务器
    emailSender = 'liuqiang053@126.com'  # 发送者邮箱
    msg = MIMEText(info)    # 邮件内容
    msg['Subject'] = subject
    msg['From'] = emailSender
    msg['To'] = emailAccepter
    smtp = smtplib.SMTP(email_host,port=25) #发送邮箱服务器和端口号
    smtp.login(emailSender, email_pwd)   # 发送者邮箱账号，密码
    smtp.sendmail(emailSender, emailAccepter, msg.as_string())# 发送者，接收者，邮件内容
    smtp.quit() # 发送完毕后退出smtp
    print (time.ctime(),'Email send success.')

#清单：时间-事情
def Todolist():
    dic = {}
    file='todolist.txt'
    with open(file,'r',encoding='utf-8') as f:
        for line in f:
            lin = line.strip().split('=')
            if len(lin) == 2:
                dic[lin[0]] = lin[1]
    return dic

def Clock():
    todolist=Todolist()
    for when,what in todolist.items():
        schedule.every().day.at(when).do(SendEmail,what)
    while True:
        schedule.run_pending()

if __name__ == '__main__':
    Clock()