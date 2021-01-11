import os
import sys
import requests
import pandas as pd
from requests_html import HTML
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def url_to_text(url, filename, save=False):
  r = requests.get(url)

  if r.status_code == 200:
    html_txt = r.text
    if save:
      with open(filename, 'w') as f:
        f.write(html_txt)
    return html_txt
  return None


def parse_and_extract(url, filename, name):
  html_str = url_to_text(url, filename)
  if html_str == None:
    return False
  html_obj = HTML(html=html_str)
  table_res = html_obj.find('.imdb-scroll-table')
  table_data = []
  headers = []

  if len(table_res) == 0:
    return False
  parse_table = table_res[0]
  rows = parse_table.find('tr')
  header_row = rows[0]
  header_cols = header_row.find('th')
  header_names = [x.text for x in header_cols]

  for row in rows[1:]:
    cols = row.find('td')
    row_data = []
    for i, col in enumerate(cols):
      row_data.append(col.text)
    table_data.append(row_data)

    path = os.path.join(BASE_DIR, 'data')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, f'{name}.csv')
    df = pd.DataFrame(table_data, columns=header_names)
    df.to_csv(filepath, index=False)
    return True


def run(start_year=None, years_ago=0):
  if start_year == None:
    start_year = datetime.now().year
  assert isinstance(start_year, int)
  assert isinstance(years_ago, int)
  assert len(f'{start_year}') == 4

  for i in range(0, years_ago+1):
    filename = os.path.join(BASE_DIR, f'world-{start_year}.html')
    url = f'https://www.boxofficemojo.com/year/world/{start_year}/'
    finished = parse_and_extract(url, filename, name=start_year)
    if finished:
      print(f'Finished {start_year}')
    else:
      print(f'{start_year} data not found ')
      
    start_year -= 1