# 03 상세 정보 코드 템플릿

import requests
from bs4 import BeautifulSoup

res = requests.get('HTML 주소')

text = res.text
print(text)

soup = BeautifulSoup(text, 'html.parser')

contents = soup.select_one('CSS 선택자').text
print(contents)