import pandas as pd
import numpy as np
# df = pd.DataFrame({'a':['happy','bthday','toyou'], 'b':[4,5,6]}, index=[1,2,3])
# print(df)

table = {'company':['abc','회사',123], '직원수':[400,10,6]}
df2 = pd.DataFrame(table)
# print(df2)
table['위치'] = ['Seoul',np.NaN, 'Busan']
df3 = pd.DataFrame(table)
# print(df3)

customerCW = {
    # 컬럼명 : 컬럼값
    'NAME': ['홍수지', '하동훈', '김지영', '최미희'],
    'ID': ['012', '013', '014', '015'],
    'AGE': [24, 32, 50, 19],
    'BALANCE': [12000000, 240000000, 420000000, 5000000],
    'GRADE': [3, 2, 1, 4]
}
import numpy as np
# customerCW['BALANCE'][0] = np.NaN
df = pd.DataFrame(customerCW)
print(df.rename(columns={'ID':'아이디', 'BALANCE':'잔고'}))
print(df)
df.rename(columns={'ID':'아이디', 'BALANCE':'잔고'}, inplace=True)
print('*******inplace 처리후****************')
print(df)

s = 'hello'
print(s.pop(0))
s = ['h']