import pandas as pd

bank = [
    {'name':'Choi','id':'1234','account':250000},
    {'name':'Park','id':'1235','account':5451000},
    {'name': 'Lee', 'id': '1236', 'account': 51000},
    {'name': 'Yoon', 'id': '1237', 'account': 8510000},
    {'name': 'Bae', 'id': '1238', 'account': 8511200},
    {'name': 'Ann', 'id': '1239', 'account': 368810}

]

df = pd.DataFrame(bank)
print(df.filter(df.account >= 350000))
# 행기준
print(df[1:3])
print(df.loc[[1,3]])
print()
print(df[df.account > 8500000])
print()
print(df[ (df.account > 8500000) & (df.name == 'Yoon') ])
print()
# print(df.filter(df.name))
print(df.iloc[:, 0:2])

df.to_csv('bank_no_head.csv', header=False)
df2 = pd.read_csv('bank_no_head.csv', header=None, names=['name','id','account'])
print(df2)
print()
df_filtered = df[['name', 'id']]
print(df_filtered)
print()
print(df.filter(items=['name', 'id']))
print()
filtered_df = df.filter(like='o', axis=1)
print(filtered_df)
# 컬럼명이 'd'로 끝나는 것들만 출력
print(df.filter(regex='d$', axis=1))
print()
print(df[df.name == '$C'])