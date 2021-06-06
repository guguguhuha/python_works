import smtplib
from email import (header)
from email.mime import (text,application,multipart)
import time

def sender_mail():
    smt_p=smtplib.SMTP()
    smt_p.connect(host='smtp.qq.com',port=25)
    sender , password = 'guguguhuha@qq.com',"********************"
    # sender , password = '2522357064@qq.com',"***************"
    smt_p.login(sender,password)
    receiver_addresses,count_num=['2805605509@qq.com'],1
#    while count_num<=3:
    for email_address in receiver_addresses:
        try:
            msg=multipart.MIMEMultipart()
            msg['from']="嘿咻"
            msg["to"]=email_address
            msg['subject']=header.Header('这是邮件主题通知','utf-8')
            msg.attach(text.MIMEText(
                '这是一封测试邮件，请勿回复本邮件~','plain','utf-8'))
            smt_p.sendmail(sender,email_address,msg.as_string())
            time.sleep(10)
            print('第%d次发给%s'%(count_num,email_address))
            count_num=count_num + 1
        except Exception as e:
            print('第%s次给%s发送邮件异常'%(count_num,email_address))
            continue
    smt_p.quit()
sender_mail()
