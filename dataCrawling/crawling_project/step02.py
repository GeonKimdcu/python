"""
네이버 날씨 미세먼지 가져오기
"""

# 1) 웹 페이지 가져오기

from bs4 import BeautifulSoup as bs # BeautifulSoup은 HTML 및 XML 파일에서 원하는 데이터를 손쉽게 Parsing 할 수 있는 라이브러리
from pprint import pprint # pprint == Pretty Print로 복잡한 자료구조의 내용을 조금 더 알기쉽게 표시해 주는 라이브러리
import requests # HTTP 요청을 보내는 라이브러리

html = requests.get('https://bit.ly/35GwYeL') # 해당 주소로 Get 요청을 하고 서버에서 응답하면 HTML코드를 받아옴
# pprint(html.text)

# 2) 파싱
# 웹 페이지는 HTML이라는 언어로 쓰여져있다. 이를 파이썬에서 쉽게 분석할 수 있도록 파싱작업을 거쳐 각 요소에 접근이 쉽게 만듬

soup = bs(html.text, 'html.parser') # 파싱하기 위해 BeautifulSoup 생성자에 해당 값을 인자로 전달 (여기선 as로 하였기 때문에 bs사용)

# 3) 크롬 개발자 도구
# F12를 이용해 현재 웹 페이지 요소 쉽게 분석 가능

# 4) 요소 1개 찾기(find) - 단일 element 검색 시
# soup.find(id='id명') / soup.find(class='class명') / # soup.find('태그 이름', class = 'class명')
"""
 미세먼지 정보가 있는 div 요소만 추출
 HTML 요소 <태그 속성 = 속성값> 텍스트가 기본 구조
 태그 : dl / 속성 : class / 속성값 : indicator
 이제 변환한 데이터에 find(태그, {속성:속성값})를 사용하여 해당 부분만 추려준다.
"""
data1 = soup.find('dl', {'class':'indicator'})
# pprint(data1)

# 5) 요소 모두 찾기(findAll) - 태그 이름을 파라미터로 전달하면 해당 태그를 전부 찾아준다.
# soup.find_all('태그 이름')
"""
 find는 처음 매칭된 1개만, findAll은 매칭된 모든 것을 반환하여 리스트로 반환 (리스트형식이기 때문에 인덱스 사용 가능)
"""
data2 = data1.findAll('dd')
# pprint(data2)

# 6) 내부 텍스트 추출
# 가운데 있는 실질적인 데이터(숫자와 단위)부분만 추출
# span 태그에 속성과 속성값은 class = "num"이다.
fine_dust = data2[0].find('span', {'class':'num'}).text  # 텍스트만 골라냄
print(fine_dust)

# 7) 초미세먼지 추출
# data2 변수에서 미세먼지는 0인덱스, 초미세먼지는 1인덱스, 오존지수는 2인덱스임
ultra_fine_dust = data2[1].find('span', {'class':'num'}).text
print(ultra_fine_dust)

# 8) 오존지수 추출
ozone = data2[2].find('span', {'class':'num'}).text
print(ozone)
