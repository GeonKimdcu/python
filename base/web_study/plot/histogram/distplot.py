import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
df_train = pd.DataFrame([ ['A01', 2, 1, 60, 139, 'country', 0, 3],
        ['A02', 3, 2, 80, 148, 'country', 0, 5],
        ['A03', 3, 4, 50, 149, 'country', 0, 7],
        ['A04', 5, 5, 40, 151, 'country', 0, 10],
        ['A05', 7, 5, 35, 154, 'city', 0, 12],
        ['A06', 2, 5, 45, 149, 'country', 0, 7],
        ['A07',8, 9, 40, 155, 'city', 1, 13],
        ['A08', 9, 10, 70, 155, 'city', 3, 13],
        ['A09', 6, 12, 55, 154, 'city', 0, 12]
    ], columns=['ID', 'hour', 'attendance', 'weight', 'iq', 'region', 'library', 'score'])

# 데이터 분석
# kde 옵션 : 밀집도 그래프, rug 옵션 : 데이터의 위치를 나타내는 선분 표시
sns.distplot(df_train['library'], kde = False, rug = True)
plt.show()

sns.distplot(df_train['library'], bins = 10, kde = False, rug = True)
plt.show()

sns.distplot(df_train['library'], hist=False, rug=True) # hist 옵션 : 히스토그램
plt.show()

sns.kdeplot(df_train['library'])
plt.show()