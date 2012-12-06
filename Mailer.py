import os, re
import sys
import smtplib
import getpass
import mimetypes
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class Mailer():
	def __init__(self, sender):
		SMTP_SERVER = 'smtp.gmail.com'
		SMTP_PORT = 587
		self.sender = sender
		self.session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		self.session.ehlo()
		self.session.starttls()
		self.session.ehlo
		password = getpass.getpass('Enter password for %s: ' % self.sender)
		self.session.login(self.sender, password)	
	
	def send_mail(self, recipient, subject, message_body, filename_with_full_path):
		directory = os.getcwd()

		msg = MIMEMultipart()
		msg['Subject'] = subject
		msg['To'] = recipient
		msg['From'] = self.sender
	
		attachment = MIMEApplication(open(filename_with_full_path, 'rb').read(), _subtype='pdf')
		attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename_with_full_path))
		msg.attach(attachment)
		msg.attach(MIMEText(message_body, 'html'))
		self.session.sendmail(self.sender, recipient, msg.as_string())

	def close(self):
		self.session.close()

