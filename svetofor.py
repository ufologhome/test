"""
Программа парсит акции Светофора
"""
import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
data = []
OFFSET = 1
BATCH_SISE = 1
PAGE_COUNT = 24
#СОБИРАЕТ ПО СТРАНИЦАМ ИНФОРМАЦИЮ
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
for item in range(1, PAGE_COUNT + 1):
    url = f'https://xn--80adbm9baodlv2b.xn--p1ai/shop/page/{item}/'
    response = requests.get(url=url, headers=headers)
    with open(f'C:\\sel\\project\\jiletki\\dataSVET\\svetofor{item}.html', 'w', \
              encoding="utf-8") as file:
        file.write(response.text)
        print(f'Мы находимся тут: {url}')
    time.sleep(5)
#СОБИРАЕТ В ПЕРЕМЕННУЮ ВСЕ СТРАНИЦЫ
for page in range(1, PAGE_COUNT + 1):
    with open(f'C:\\sel\\project\\jiletki\\dataSVET\\svetofor{page}.html', 'r', \
              encoding="utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    cards = soup.findAll('div', class_='content-item-product')
    print(len(cards))
    for card in cards:
        try:
            CARD_A = card.find('div', class_='title-content-item-product').text.strip()
        except:
            CARD_A = '-'
        try:
            CARD_B = card.find('div', class_='price-content-item-product').text.strip()
        except:
            CARD_B = '-'
        print(CARD_A)
        print(CARD_B)
