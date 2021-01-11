from flask import Flask
from scraper import run as scrape_runner
from logger import logger

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_view():
  return "Hello world this is from flask"


@app.route('/abc', methods=['GET'])
def abc_view():
  return "Hello Flask from abc view"


@app.route('/box-office-mojo', methods=['GET'])
def box_office_scrapper():
  logger()
  scrape_runner()
  return {"process": "Done"}