"""
Scraping the dixy.ru
"""
import datetime
import time
from selenium.webdriver import FirefoxOptions
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

data = []

opts = FirefoxOptions()
##opts.add_argument("--headless")
opts.page_load_strategy = 'none'
fp = webdriver.FirefoxProfile('C:\\Users\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\...') # Ваш профиль firefox
driver = webdriver.Firefox(options=opts, firefox_profile=fp)

try:
    start_time = datetime.datetime.now()
    OFSET = 1
    SHAG = 1

    while True:
        for item in range(OFSET, OFSET + SHAG, 1):
            OFSET += SHAG
            url = f"https://dixy.ru/catalog/?PAGEN_1={item}"
            print(f'Мы находимся тут: {url}')
            driver.get(url)
            time.sleep(10)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        cards = soup.find_all('div', class_='product-container')
        cardss = soup.findAll('div', class_='product-container')

        for card in cardss:
            try:
                CARD_TITLE = card.find('div', class_='dixyCatalogItem__hover').text.strip()
            except:
                CARD_TITLE = '-'
            try:
                CARD_TITLE = card.find('div', class_='dixyCatalogItem__title').text.strip()
            except:
                CARD_TITLE = '-'
            try:
                CARD_DISCOUNT = card.find('div', class_='dixyCatalogItemPrice__discount'). \
                                text.strip()
            except AttributeError:
                continue
            try:
                CARD_PRISE_OLD_INTEGER = card.find('div', class_='dixyCatalogItemPrice__oldp \
                                         rice').text.strip()
            except AttributeError:
                continue
            try:
                CARD_PRICE_NEW = card.find('div', class_='dixyCatalogItemPrice__new').text.strip()
            except AttributeError:
                continue
            try:
                CARD_SALE_DATE = card.find('div', class_='dixyCatalogItem__term') \
                                 .text.strip() #.replace('\n', ' ')
            except AttributeError:
                continue
        new = ((CARD_TITLE,CARD_DISCOUNT,CARD_PRISE_OLD_INTEGER,CARD_PRICE_NEW,CARD_SALE_DATE))
        data.append(new)

        if len(cards) < 16:
            break
    finish_time = datetime.datetime.now()
    spent_time = finish_time - start_time

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

df = pd.DataFrame(data,columns=['Продукт', 'Процент скидки', 'Старая цена', \
                                'Новая цена', 'Время акции'])
df.to_csv('Akcii-14.06.22.csv')
print(f"Фаил CSV был сделан за {spent_time}")
