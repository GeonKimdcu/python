from bs4 import BeautifulSoup
from pprint import pprint
import requests

# 웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

# 월요일 웹툰영역 추출하기
data1 = soup.find('div',{'class':'col_inner'})
# pprint(data1)

# 제목 영역 코드 추출하기
data2 = data1.findAll('a', {'class':'title'})
# pprint(data2)

# for를 이용한 text 추출
'''
title_list = []
for t in data2:
    title_list.append(t.txt)

pprint(title_list)
'''

# text만 추출
title_list = [t.text for t in data2]
# pprint(title_list)

# 모든 요일 웹툰 제목 추출하기
# 요일별 영역 가져오기
data1_list = soup.findAll('div', {'class':'col_inner'})
#pprint(data1_list)

# 하나의 리스트로 묶기
# 요일별 title_list가 생성될 때 마다 특정 리스트에 저장하도록 코딩
# 전체 웹툰 리스트
week_title_list = []

# 이하 코드 반복시키기
for data1_1 in data1_list:
    # 제목 포함 영역 출력하기
    data2_list = data1_1.findAll('a', {'class':'title'})
    # pprint(data2_list)

# 텍스트만 출력
title_list_2 = [t.text for t in data2_list]
# pprint(title_list_2)
# week_title_list.extend(title_list) # 단순하게 값을 추가해 1차원적으로 만들 때
week_title_list.append(title_list) # 요일별로 나눠 2차워적으로 만들 때
pprint(week_title_list)

# 웹툰 제목 가져오는 코드 단순화

# 웹 페이지를 읽고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

#모든 웹툰 제목 영역 추출
data1=soup.findAll('a',{'class':'title'})
week_title_list = [ t.text for t in data1]
pprint(week_title_list)

''' 1번째 방법은 영역을 나눠서 접근하는 방법
    2번째 방법은 단순하게 모든 영역에 접근하는 방법임'''