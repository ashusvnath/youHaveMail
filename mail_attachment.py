import os, re
import sys
import smtplib
import getpass
import mimetypes
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer():
	def __init__(self, mail_id, filename):
		SMTP_SERVER = 'smtp.gmail.com'
		SMTP_PORT = 587
		self.sender = 'vishwas@thoughtworks.com'
		self.session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		self.session.ehlo()
		self.session.starttls()
		self.session.ehlo
		password = getpass.getpass('Enter password for %s: ' % sender)
		self.session.login(sender, password)	
	
	def sendMail(self, recipient, message_body, filename_with_full_path):
		recipient = 'vaikuntj@thoughtworks.com'
		directory = os.getcwd()

		msg = MIMEMultipart()
		msg['Subject'] = 'Your Mobile bill for the %s - %s' % (start_date, end_date)
		msg['To'] = recipient
		msg['From'] = self.sender
	
		attachment = MIMEApplication(open(filename_with_full_path, 'rb').read(), _subtype='pdf')
		attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename_with_full_path))
		msg.attach(attachment)
		msg.attach(MIMEText(message_body))
		self.session.sendmail(sender, recipient, msg.as_string())

