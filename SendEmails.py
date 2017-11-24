#sample send gmail
#/home/mahbooda/Desktop/Hertz App PPT.pptx

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from_mail = 'mahabooda580@gmail.com'
email_password = 'manzoorali1'
to_mail = 'sk.manzoor580@gmail.com'

subject = 'This is Python Sample !!!!!'

msg = MIMEMultipart()
msg['From'] = from_mail
msg['To'] = to_mail
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

filename='/home/mahbooda/Desktop/mechanic_person.png'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(from_mail,email_password)


server.sendmail(from_mail,to_mail,text)
print('mail sent')
server.quit()

