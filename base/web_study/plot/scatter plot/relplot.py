import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
df_train = pd.DataFrame([
        ['A01', 2, 1, 60, 139, 'country', 0, 'fail'],
        ['A02', 3, 2, 80, 148, 'country', 0, 'fail'],
        ['A03', 3, 4, 50, 149, 'country', 0, 'fail'],
        ['A04', 5, 5, 40, 151, 'country', 0, 'pass'],
        ['A05', 7, 5, 35, 154, 'city', 0, 'pass'],
        ['A06', 2, 5, 45, 149, 'country', 0, 'fail'],
        ['A07',8, 9, 40, 155, 'city', 1, 'pass'],
        ['A08', 9, 10, 70, 155, 'city', 3, 'pass'],
        ['A09', 6, 12, 55, 154, 'city', 0, 'pass']
    ], columns=['ID', 'hour', 'attendance', 'weight', 'iq', 'region', 'library', 'pass'])

# 데이터 분석
sns.relplot(x='hour', y = 'attendance', data = df_train)
plt.show()

sns.relplot(x='hour', y='attendance', data=df_train, hue = 'pass')
plt.show()

df_temp = df_train.copy()
df_temp['pass'] = df_temp['pass'].replace([0,1], ['fail', 'pass'])
sns.relplot(x='hour', y='attendance', data = df_temp, hue = 'pass')
plt.show()