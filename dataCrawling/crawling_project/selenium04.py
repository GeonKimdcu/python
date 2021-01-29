from selenium import webdriver
import time

# 클립 영상 소스링크
driver = webdriver.Chrome('chromedriver')
driver.get('https://www.twitch.tv/soorte214/clip/AgileGracefulCheesecakePeteZarollTie') # 특정 클립 링크

time.sleep(3)

# video 태그 확인
url_element = driver.find_element_by_tag_name('video')
vid_url = url_element.get_attribute('src')
print(vid_url)

# 영상 제목과 날짜 추출
title_element1 = driver.find_element_by_class_name('tw-flex')
title_element2 = title_element1.find_elements_by_tag_name('span')
vid_title = None
vid_date = None
for span in title_element2:
    try:
        d_type = span.get_attribute('data-test-selector')
        if d_type == 'title':
            vid_title = span.text
        elif d_type == 'date':
            vid_date == span.text
    except:
        pass

print(vid_title, '\t', vid_date)

# 특수문자 없애고 빈칸도 없애기
import re
vid_title = re.sub('[^0-9a-zA-Zㄱ-힐]', '', str(vid_title)) # 추출할 리스트가 string형식이어야해서 str로 형변환
vid_date = re.sub('[^0-9a-zA-Zㄱ-힐]', '', str(vid_date))
print(vid_title, '\t', vid_date)

from urllib.request import urlretrieve
urlretrieve(vid_url, vid_title+'_'+vid_date+'.mp4')

driver.close()