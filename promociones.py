import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def getSoup(url, header):
    response = requests.get(url, headers=header)
    return BeautifulSoup(response.text, "html.parser")

def getText(str):
    item = ''
    i = 0
    while str[i] != '>':
         i += 1
    i += 1
    while str[i] != '<':
        item += str[i]
        i+=1
    return item

def scrapeAdidas():
    url = 'https://www.adidas.com/us/women-shoes'
    header = {
        'User-Agent': 'My User Agent 1.0', 
        'From': 'youremail@domain.com'
    } 
    soup = getSoup(url, header)

    # browser = webdriver.Chrome()
    # browser.get(url)
    # nav = browser.find_element_by_id("gl-price__value")
    # print(nav.text)

    # print(soup.find_all("div", class_="gl-product-card__details-main"))
    products = {}

    for div in soup.find_all("div", class_="gl-product-card__details-main"):
        print(div.text)
        # for name in div.find_all("div", class_="gl-product-card__name gl-label gl-label--m"):
        #     print("Name:" + name.text)
        # for price in div.find_all("div", class_="gl-price gl-price--s gl-price__inline___-VD1g"):
        #     print("Price:" + price.text)

    for price in soup.find_all("span", class_="gl-price__value"):
        print(price)

    count = 1
    for i in soup.findAll('title'):
        products['Adidas '+ str(count)] = getText(str(i))
        count += 1
    return products

yeezyProducts = scrapeAdidas()

# print (yeezyProducts)