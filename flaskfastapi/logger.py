import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def logger():
  logs = os.path.join(BASE_DIR, 'logs')
  os.makedirs(logs, exist_ok=True)
  logger = os.path.join(logs, f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}.txt')

  with open(logger, 'w') as f:
    f.write(f'{datetime.now()}')