import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path('index.html').read_text())
email=EmailMessage()
email['from']='Palash'
email['to']='palashhwpaul@gmail.com'
email['subject']='Yo won the game!'

email.set_content(html.substitute({'name':'Hawee'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('testingpython92@gmail.com','pythontest123')
	smtp.send_message(email)
	print('All is well!')
