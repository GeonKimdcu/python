import requests
from bs4 import BeautifulSoup as bs

headers = {
    'Referer' : 'https://www.naver.com/'
}
res = requests.get('https://www.naver.com/', headers = headers)
print(res)

text = res.text

soup = bs(text, 'html.parser')
print(soup)

