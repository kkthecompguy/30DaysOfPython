import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


username = "hnkhosamomollo@gmail.com"
password = 'khosam7054'
host = 'smtp.gmail.com'
port = 587
pwd = 'wwqxfbkjfdzrbjdx'


def send_mail(text="This is mail is being sent by a python program", subject="Automating everything with Python", from_email="Kosamtech Python <hnkhosamomollo@gmail.com>", to_emails=None, html='<p>This is mail is being sent by a python program</p>'):
  assert isinstance(to_emails, list)

  msg = MIMEMultipart('alternative')
  msg['From'] = from_email
  msg['To'] = ", ".join(to_emails)
  msg['Subject'] = subject

  txt_part = MIMEText(text, 'plain')
  msg.attach(txt_part)

  if html != None:
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)

  msg_str = msg.as_string()

  with smtplib.SMTP(host=host, port=port) as server:
    server.ehlo()
    server.starttls()
    server.login(username, pwd)
    server.sendmail(from_email, to_emails, msg_str)

send_mail(to_emails=['kosamdjango@gmail.com', 'christineoguk105@gmail.com', 'hnkhosamomollo3@gmail.com'])

to_emails=['kosamdjango@gmail.com', 'christineoguk105@gmail.com', 'hnkhosamomollo3@gmail.com']