import smtplib,ssl
import socket
from smtplib import SMTP_SSL
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import sys

def sendmail():

    mailmessage = sys.argv[1]
    email_sender = '703272279@genpact.com'
    messageinp = mailmessage
    email_recipientinp = 'vibhor.saxena@genpact.com'
    subject = 'Your SSH PrivateKey value for ssh to AzureVM using SSH Authn'

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipientinp
    msg['Subject'] = subject
    msg.attach(MIMEText(messageinp, 'plain'))

    try:
      server = smtplib.SMTP('smtp.office365.com', 587)
      server.ehlo()
      server.starttls()
      server.login('703272279@genpact.com', 'June@2023') #'JaiShiv@2021')
      text = msg.as_string()
      server.sendmail(email_sender, email_recipientinp, text)
      print('email sent')
      server.quit()
    except Exception as e:
      print("SMPT server connection error"+ str(e))
      return False
    return True




if __name__ == "__main__":
    sendmail()
