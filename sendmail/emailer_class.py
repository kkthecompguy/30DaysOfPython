import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Emailer():
  username = 'kosamdjango@gmail.com'
  pwd = 'oxmsxfilrsadinkc'
  host = 'smtp.gmail.com'
  port = 587
  from_email = 'Kosamtech Python <kosamdjango@gmail.com>'

  def __init__(self, subject, text, html, from_email=from_email, to_emails=[]):
    self.from_email = from_email
    assert isinstance(to_emails, list)
    self.to_emails = to_emails
    self.subject = subject
    self.text = text
    self.html = html


  def send_mail(self):
    with smtplib.SMTP(host=self.host, port=self.port) as server:
      server.ehlo()
      server.starttls()
      server.login(self.username, self.pwd)
      server.sendmail(self.from_email, self.to_emails, self.format_msg())


  def format_msg(self):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = self.subject
    msg['From'] = self.from_email
    msg['To'] = ', '.join(self.to_emails)

    text_part = MIMEText(self.text, 'plain')
    msg.attach(text_part)

    if self.html != None:
      html_part = MIMEText(self.html, 'html')
      msg.attach(html_part)
    
    msg_str = msg.as_string()
    return msg_str


