import os
from inbox import read_inbox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

fname = os.path.join(BASE_DIR, 'inbox.txt')

def save_inbox_data(my_messages, filename = None):
  assert filename is not None

  with open(filename, 'w') as file:
    if len(my_messages) != 0:
      for data in my_messages:
        file.write(data['subject'] + '\n')
        file.write(data['from'] + '\n')
        file.write(data['to'] + '\n')
        file.write(data['date'] + '\n')
        file.write(data['body'] + '\n')
      return True
    return False


my_messages = read_inbox()
print(my_messages)
save_inbox_data(my_messages, filename=fname)