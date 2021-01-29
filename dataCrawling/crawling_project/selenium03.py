from selenium import webdriver
from pprint import pprint
import time
from collections import Counter

# 웹 페이지 코드 분석
driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(300)

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')
# print(len(btns))
def analysis():
    btns_rgba = [btn.value_of_css_property('background-color') for btn in btns]
    result = Counter(btns_rgba)
    for key, value in result.items():
        # value가 1인 것 탐색
        if value == 1:
            answer = key
            break
    else:
        answer = None
        print("정답을 찾을 수 없습니다.")

    if answer:
        index = btns_rgba.index(answer)
        btns[index].click()

# 정답 탐색하기
'''
 1. 각 div의 rgba값 추출
 2. 추출한 rgba중 값 하나 다른 곳이 정답
'''

# 디자인 정보(css) 추출
''' 
css란 html 요소의 디자인 속성 정보
모든 버튼에 대해 배경색상 정보를 추출하여 리스트에 저장
'''
# btns_rgba = [btn.value_of_css_property('background-color')for btn in btns]
# pprint(btns_rgba)

# result = Counter(btns_rgba)
# pprint(result) # 여기서 value가 1인게 정답

# 정답 찾기
'''
collections 모듈의 Counter함수를 이용
'''
# value가 1인 것 탐색
'''for key, value in result.items():
    if value == 1:
        answer = key
        break
else:
    answer = None
    print("정답을 찾을 수 없습니다.")'''

# 정답 클릭
'''
1. btns_rgba에서 인덱스 값을 구한다.
2. 그 인덱스 값으로 btns 인덱스에 접근, 클릭
'''
'''if answer:
    index = btns_rgba.index(answer)
    btns[index].click()'''

# 제한시간동안 수행
''' 
time.time()은 UTC기준부터 현재까지의 시간을 초로 반환.
이를 이용해 60초가 지났는지 확인해준다.
'''
if __name__=="__main__":
    start = time.time()
    while time.time()-start <= 60:
        analysis()

# 다른 방법
'''
웹 페이지 소스코드를 분석해보면 정답 버튼은 class = "main" 속성과 속성값을 가지고 있음.
from selenium import webdriver
from pprint import pprint
import time

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicity_wait(300)

# 시작 시각
start = time.time

while time.time() - start <= 60:
    try:
        btns = driver.find_element_by_class_name("main")
        btn.click()
    except:
        pass
'''