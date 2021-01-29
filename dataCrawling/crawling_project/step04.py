# 네이버 웹툰 썸네일 가져오기

# 제목과 썸네일이 같이 존재하는 영역
import errno # 예외처리(try -except) 위한 라이브러리
from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os  # re는 정규 표현식 지원 모듈, os는 운영체제에서 제공되는 기능 지원 모듈
from urllib.request import urlretrieve # urlretrieve는 이미지 다운로드 지원 모듈

# 저장 폴더 생성
try:
    if not (os.path.isdir('image')):  # os.path.isdir("있는지 없는지 검사할 폴더 경로")
        os.makedirs(os.path.join('image')) # os.makedirs는 폴더 생성 함수 / os.path.join은 경로를 병합하여 새 경로 생성
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()

# 웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

# 요일별 웹툰영역 출력하기
data1_list = soup.findAll('div',{'class':'col_inner'})
# pprint(data1_list)

# 전체 웹툰 리스트
li_list = []
for data1 in data1_list:
    # 제목+썸네일 영역 추출
    li_list.extend(data1.findAll('li')) # 해당 부분을 찾아 li_list와 병합

# pprint(li_list)

# 제목과 이미지 링크 출력
""" li 요소를 보면 img 태그에 썸네일 이미지의 주소와 웹툰 제목이 속성값으로 존재함.
img 태그를 추출한 뒤 속성값을 추출 -> 추출한 데이터에 ['속성명']을 적으면 됨. """
# 각각 썸네일과 제목 추출하기
for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src'] # src는 이미지 링크
    # print(title, img_src)
    # 다운로드하기 (특수문자 제거해 다운로드 오류 발생 제거)
    title = re.sub('[^0-9a-zA-Zㄱ-힐]', '', title) # 글자가 아닌 것은 ''로 치환시킴 
    # re.sub(pattern, repl, string) : string에서 pattern과 매치하는 텍스트를 repl로 치환
    urlretrieve(img_src, './image/'+ title+'.jpg') # 주소, '파일경로 + 파일명 + 확장자'
    # urllib.request.urlretrieve(url, full_name)에서 url이 가리키는 주소에 접근해서 해당 자원을 full_name에 정의한 경로와 이름으로 저장
