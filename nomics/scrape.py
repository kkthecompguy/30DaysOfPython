import os
import requests
import pandas as pd
from requests_html import HTML

BASE_DIR = os.path.dirname(os.path.abspath(__file__))



def url_to_text(url, save=False):
  res = requests.get(url)
  if res.status_code == 200:
    html_str = res.text
    if save:
      with open('nomics.html', 'w') as f:
        f.write(html_str)
    return html_str


def parse_and_extract(url, page_num=None):
  table_data = []
  html_str = url_to_text(url)
  html_obj = HTML(html=html_str)
  table_el = html_obj.find('table')
  parsed_table = table_el[0]
  rows = parsed_table.find('tr')
  header_row = rows[0]
  header_cols = header_row.find('th')
  header_names = [x.text for x in header_cols]
  for i, x in enumerate(header_names):
    if x == '':
      header_names[i] = 'New header'
    else:
      header_names[i] = x


  for row in rows[2:]:
    row_data = []
    cols = row.find('td')
    for i, col in enumerate(cols):
      row_data.append(col.text)
    table_data.append(row_data)

    
    path = os.path.join(BASE_DIR, 'data')
    os.makedirs(path, exist_ok=True)
    if page_num != None:
      filename = os.path.join(path, f'currency-{page_num}.csv')
    else:
      filename = os.path.join(path, 'currency.csv')
    df = pd.DataFrame(table_data, columns=header_names)
    df.to_csv(filename, index=False)
  print(f'Finished saving page {page_num}')
  return True

for i in range(2, 60+1):
  url = f'https://nomics.com/{i}'
  parse_and_extract(url, page_num = i)