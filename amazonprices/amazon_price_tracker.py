
import re
import os
import requests
import time
import pandas as pd
from requests_html import HTML
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

cwd = os.getcwd()
BASE_DIR = os.path.join(cwd) 
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)
product_output = os.path.join(DATA_DIR, 'products.csv')
product_categories_links_ouput = os.path.join(DATA_DIR, 'product-catgories.csv')

categories = [
    {"name": "computers_and_accessories", "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225009011&rh=n%3A%2116225009011%2Cn%3A541966&ref=nav_em__nav_desktop_sa_intl_computers_and_accessories_0_2_5_6"},
    {"name": "data_storage", "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A1292110011&ref=nav_em__nav_desktop_sa_intl_data_storage_0_2_6_5"},
    {"name": "clothing", "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A1040658&ref=nav_em__nav_desktop_sa_intl_clothing_0_2_13_2"}
]

def extract_page_links(url):
    driver.get(url)
    time.sleep(2)
    body = driver.find_element_by_css_selector('body')
    html_str = body.get_attribute('innerHTML')
    html_obj = HTML(html=html_str)
    links = html_obj.links
    return links


def extract_product_id_from_url(url):
    product_id = None
    regex_pattern = "https://amazon.com/(?P<slug>[\w-]+)/dp/(?P<product_id>[\w-]+)/"  
    regex = re.compile(regex_pattern)
    match = regex.match(url) 
    if match != None:
        try:
            product_id = match['product_id']
        except:
            pass
    return product_id

def clean_page_links(links=[]):
    final_page_links = []
    for link in links:
        product_id = extract_product_id_from_url(link)
        if product_id != None:
            final_page_links.append({'product_id':product_id, 'url': link}) 
    return final_page_links  

def scrape_category_page_links(categories=[]):
    all_page_links = []
    for category in categories:
        time.sleep(2)
        url = category.get('url')
        page_links = [f'https://amazon.com{x}' for x in extract_page_links(url) if x.startswith('/')] 
        cleaned_links = clean_page_links(links=page_links)
        all_page_links += cleaned_links
    return all_page_links

all_product_links = scrape_category_page_links(categories=categories)
# category_df = pd.DataFrame(all_product_links)
# category_df.to_csv(product_categories_links_ouput, index=False)
all_product_links

category_df = pd.DataFrame(all_product_links)
category_df.to_csv(product_categories_links_ouput, index=False)

def scrape_product_page(url, title_lookup="#productTitle", price_lookup="#priceblock_ourprice"):
    driver.get(url)
    time.sleep(3)
    body = driver.find_element_by_css_selector('body')
    html_str =  body.get_attribute('innerHTML')
    html_obj = HTML(html=html_str)
    product_title = html_obj.find(title_lookup, first=True).text
    product_price = html_obj.find(price_lookup, first=True).text
    return product_title, product_price

def perform_scrape(links):
    extracted_data = []
    for link in links:
        product_id = link['product_id']
        title, price = (None, None)
        url = link['url']
        try:
            title, price = scrape_product_page(url)
        except:
            pass
        if title != None and price != None:
            print(title, price)
        product_data = {
            'title': title,
            'price': price,
            'productId': product_id,
            'url': url
        }
        extracted_data.append(product_data)
    return extracted_data

data_extracted = perform_scrape(all_product_links)
df = pd.DataFrame(data_extracted)
df.to_csv(output, index=False)
