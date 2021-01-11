from fastapi import FastAPI
from scraper import run as scrape_runner
from logger import logger

app = FastAPI()

@app.get('/')
def hello_view():
  return {"hello": "Hello world this is from FastAPI"}


@app.get('/abc')
def abc_view():
  return {"hello": [1, 3, 4, "hello world"]}


@app.get('/box-office-mojo')
def box_office_scraper():
  logger()
  scrape_runner()
  return {"process": "Done"}