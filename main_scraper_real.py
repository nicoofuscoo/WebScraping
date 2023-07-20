import ssl
from bs4 import BeautifulSoup
import requests

html_page = requests.get('https://store.nintendo.co.uk/en_gb/merchandise/view-all-merchandise/').text

soup = BeautifulSoup(html_page, 'lxml')

item = soup.find_all("a", class_="card__link js-gtm-product-click-elem")

for i in item:
    #only find mario items
    title = i.find("h2", class_="card__title").text.strip()
    if 'Mario' in title:

        price = i.find("div", class_="card__price").text.strip()

        print(f'''
            Name: {title}
            Price: {price}
            ''')
    