import requests
from bs4 import BeautifulSoup
import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = 'alragnarok$201##'
except KeyError:
    SOME_SECRET = "Token not available!"
    logger.info("Token not available!")
    

if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")
    url = requests.get('https://serbasepeda.com/')
    soup = BeautifulSoup(url.text, 'html.parser')

    featureP = soup.find('div', 'page-dis')
    items = featureP.find_all('li', 'item')

    for item in items:
        title = item.find('p','title').text
        price = item.find('p', 'price-member').text

        print(title, price)

