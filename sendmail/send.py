import sys
from send_mail import send_mail

def send(name, to_emails=None):
  assert isinstance(to_emails, list)

  try:
    send_mail(to_emails=to_emails)
    print('Mail sent')
  except:
    print('Mail not sent')


name = ""
to_emails = []

if len(sys.argv) > 1:
  name = sys.argv[1]
if len(sys.argv) > 2:
  to_emails.append(sys.argv[2])
if len(sys.argv) > 3:
  to_emails.append(sys.argv[3])
send(name, to_emails=to_emails)
