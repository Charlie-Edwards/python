import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import sys
import os

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.ehlo()

load_dotenv()

if os.path.exists('.env'):
    email = os.getenv('EMAIL')
    email = email.strip()
    password = os.getenv('PASSWORD')
    password = password.strip()
    recipient = input("Enter recipients email address: ")
    name = input("Enter your name: ")
    subject = input("Enter email subject: ")
else:
    print('enter email and password in the .env file')
    sys.exit()

server.login(email, password)

msg = MIMEMultipart()
msg['From'] = name
msg['To'] = recipient
msg['Subject'] = subject

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

p = MIMEBase('application', 'octet-stream')

text = msg.as_string()
server.sendmail(email, recipient, text)
