from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = "https://www.python.org"
#url = "https://www.adidas.pe"

req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})


web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')

res = BeautifulSoup(web_byte.decode(),"html.parser")
print(webpage)