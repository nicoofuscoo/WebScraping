from bs4 import BeautifulSoup

with open ('page_example.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')

    site_cards = soup.find_all('div', class_="card")

    for items in site_cards:
        card_title = items.h1.text
        card_subtitle = items.p.text
        print(f'{card_title} has subtitle {card_subtitle}')