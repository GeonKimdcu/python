# 01 HTML 받아오기 코드 템플릿
import requests

res = requests.get('HTML 주소')

text = res.text
print(text)