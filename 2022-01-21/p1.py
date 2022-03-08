import pandas as pd
from collections import OrderedDict
friends = [
    [20, 'Han', 'JeongMin'],
    [25, 'Park', 'YooHyuk']
]

columns_name = ['age', 'firstName', 'LastName']

df = pd.DataFrame(friends, columns=columns_name)

print(df)
# 나이가 20살 이하인 사람만 가져오고 싶음
print('******under age 20******')
print(df[df.age<=20])
print(df.query('age<=20'))
print('*****df*****')
print(df)
print(df.firstName)
print("***under 25 and first name is Han***")
print(df[(df.age <=25) & (df.firstName == 'Han')])

friends2 = [
    [20, 'Han', 'JeongMin'],
    [25, 'Park', 'Yoohyuk'],
    [30, 'Choi', 'SooKyung']
]

df2 = pd.DataFrame.from_records(friends2)
print('******df2******')
# age 정보를 모두 삭제하고 싶음 : 행은 다 살리고 열중에 age 제거
print(df2.iloc[:,1:])
# 0번 행과 2번 행만 가져오고 싶음
print(df2.iloc[[0,2]])

ordered_dict = OrderedDict([
    ('age', [20, 25]),
    ('firstName', ['Han', 'Park']),
    ('LastName', ['JeongMin', 'YooHyuk'])
])

df3 = pd.DataFrame.from_dict(ordered_dict)
print(df3)

friends4 = [
    {'age': 20, 'firstName': 'Han', 'lastName': 'JeongMin'},
    {'age': 25, 'firstName': 'Park', 'lastName':'YooHyuk'}
]

df4 = pd.DataFrame(
    friends4
)

print(df4)
print('****switch column name!****')
df4 = df4[['firstName', 'lastName', 'age']]
print(df4)

# 헤더 정보 제거하고 csv 파일 만들기
# df4.to_csv('friends.csv', header=False)
# index 값 제거하고 csv 파일 만들기
# df4.to_csv('friends.csv', index=False)
# 둘다 제거하기
# df4.to_csv('friends.csv', index=False, header=False)
