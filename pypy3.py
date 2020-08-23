import smtplib
smtp=smtplib.SMTP_SSL('smtp.gmail.com',465)
smtp.ehlo()
smtp.login('myemail','passwd')
from email.message import EmailMessage
msg=EmailMessage()
msg['Subject']='email_subject'
msg['from']='myemail'
msg['To']='target email'
msg.set_content('메일본문')
smtp.send_message(msg)
