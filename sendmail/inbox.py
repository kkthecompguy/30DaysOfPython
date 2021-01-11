import imaplib
import email

# username = "hnkhosamomollo@gmail.com"
username = 'kosamdjango@gmail.com'
# pwd = 'wwqxfbkjfdzrbjdx'
pwd = 'oxmsxfilrsadinkc'
host = 'imap.gmail.com'

def read_inbox():
  with imaplib.IMAP4_SSL(host) as mail:
    mail.login(username, pwd)
    mail.select(('inbox'))
    _, search_data = mail.search(None, 'UNSEEN')

    my_messages = []

    for num in search_data[0].split():
      email_data = {}

      _, data = mail.fetch(num, ('RFC822'))
      _, b = data[0]
      email_message = email.message_from_bytes(b)

      for header in ['subject', 'to', 'from', 'date']:
        print("{}: {}".format(header, email_message[header]))

        email_data[header] = email_message[header]

      for part in email_message.walk():
        if part.get_content_type() == 'text/plain':
          body = part.get_payload(decode=True)
          email_data['body'] = body.decode()
        if part.get_content_type() == 'text/html':
          html_body = part.get_payload(decode=True)
          email_data['html_body'] = html_body.decode()
      my_messages.append(email_data)
    return my_messages
