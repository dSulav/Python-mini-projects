import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['myemail@gmail.com','test@example.com']
msg = EmailMessage()
msg['Subject'] = 'New python project'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ','.join(contacts)
msg.set_content('Image Attached')

files = ['pypro1.png','pypro2.png']

for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        file_name = f.name

msg.add_attachement(file_data,maintype='application',subtype='octet-stream', filename=file_name)
    

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_PASSWORD,EMAIL_PASSWORD)
    smtp.send_message(msg)
    