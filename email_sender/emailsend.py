'''   
  IMPORTANT NOTE : impot all the modules before running the code
'''
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'your names'
email['to'] = 'receiver emailadress'
email['subject'] = 'subject of email'

email.set_content(html.substitute({'name': 'receiver name'}), 'html')   # connects with html page

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:    # server call
  smtp.ehlo()
  smtp.starttls()
  smtp.login('your email id', 'your password')
  smtp.send_message(email)
  print('all good boss!')
