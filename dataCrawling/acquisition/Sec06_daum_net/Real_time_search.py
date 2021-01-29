import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.daum.net/')

text = res.text


soup = BeautifulSoup(text, 'html.parser')


for li in soup.select('#mArticle > div.cmain_tmp > div.section_media >'
                      ' div.hot_issue.issue_mini > div.hotissue_layer >'
                      ' ol > li'):
    rank = li.span.span.text
    keyword = li.a.text
    print(rank, keyword)