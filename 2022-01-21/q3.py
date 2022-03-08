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
# df = df.drop([0,5])
# df 에 담지않고 바로 assign 하는 방법
# df.drop([0,5], inplace=True)
# print(df)
df = df.drop(df.index[[0,1]])
print(df)
print()
df = pd.DataFrame(bank)
print(df)
