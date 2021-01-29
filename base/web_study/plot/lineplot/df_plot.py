import numpy as np
import pandas as pd
from fbprophet import Prophet # 시계열 예측할 때 사용
import matplotlib.pyplot as plt

#Load Dataset

df = pd.read_csv('https://raw.githubusercontent.com/kairess/forecast_avocado_prices/master/avocado.csv')

df.head()
df.describe() # 요약된 통계 결과 반환

#Types
df.groupby('type').mean()  # 'type'별로 grouping하여 평균 값 산출

#Preprocess [전처리]
# 'type'이 'conventional'이면서 'region'이 'TotalUS'인 값을 가지는 모든 행을 df 값에 저장
df = df.loc[(df.type == 'conventional')&(df.region == 'TotalUS')]
# pd.to_datetime 함수를 쓰면 날짜/시간을 나타내는 문자열을 자동으로 datetime 자료형으로 바꾼 후 DatetimeIndex 자료형 인덱스 생성
df['Date'] = pd.to_datetime(df['Date'])
# 'Date', 'AveragePrice'의 인덱스를 리셋시키고 drop = True이기 때문에 인덱스로 세팅한 행 제외하곤 다 삭제
data = df[['Date', 'AveragePrice']].reset_index(drop = True)
# 시계열 데이터 생성
data = data.rename(columns = {'Date':'ds', 'AveragePrice':'y'})  # 시계열 ds(datestamp) / 입력하고 예측하고자 하는 값 y
data.head()

# 시각화
data.plot(x='ds', y = 'y',figsize=(16,8)) # figsize(16,8)은 가로 16 세로 8을 인자로하는 크기의 그래프 출력
plt.show()