# 02 목록 코드 템플릿

import requests
from bs4 import BeautifulSoup

res = requests.get('HTML 주소')

text = res.text
print(text)

soup = BeautifulSoup(text, 'html.parser')

for li in soup.select('CSS 선택자'):
    title = li.a.text # title = li.select_one('a).text
    url = li.a['href']
    print(title, url)