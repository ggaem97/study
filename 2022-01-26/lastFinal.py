import pandas as pd

customer = [
    {'name': '한정민', 'age': 26, 'address': 'Ansan', 'account':85000000},
    {'name': '박우혁', 'age': 29, 'address': 'Soowon', 'account':95211001},
    {'name': '김설준', 'age': 25, 'address': 'Dokyo', 'account':151000215},
    {'name': '존리', 'age': 58, 'address': 'Bucheon', 'account':5554422100},
    {'name': '최인수', 'age': 30, 'address': 'Incheon', 'account':52200005},
    {'name': '유재석', 'age': 45, 'address': 'Seoul', 'account':88112155500}
]
# df = pd.DataFrame(customer, columns=['name', 'age', 'address', 'account'])

# 0번째 행 제거하기
# print(df.drop([0]))
# df = df.drop(df.index[[0]])


# print(df.drop(df.index[0]))
# print()
# 0번째 행 제거하면서 할당하기
# df.drop([0], inplace=True)
# print(df)

# age 컬럼 제거하기
# print(df.drop('age', axis=1))

# 성별 컬럼 female로 추가하기
# df['sex'] = 'female'
# print(df)

# 한정민만 성별을 여자, 나머지는 남자로 지정하기
# import numpy as np
# df['sex'] = np.where(df.name == '한정민', 'female', 'male')
# df['sex'] = np.where(df['name'] == '한정민', 'female', 'male')
# print(df)

student = [
    {'name': '한정민', 'sqld': 98, 'adsp': 88, 'sqlp':100},
    {'name': '박우혁', 'sqld': 100, 'adsp': 100, 'sqlp':90},
    {'name': '아이유', 'sqld': 35, 'adsp': 85, 'sqlp':69},
    {'name': '최수경', 'sqld': 80, 'adsp': 62, 'sqlp':99},
    {'name': '안철수', 'sqld': 100, 'adsp': 80, 'sqlp':100},
    {'name': '전지현', 'sqld': 54, 'adsp': 75, 'sqlp':50}
]


df = pd.DataFrame(student)
df = df[['name', 'sqld', 'sqlp', 'adsp']]
# print(df)

# sqld + sqlp 에 대한 total 점수 구하기
df['total'] = df['sqld'] + df['sqlp']
# print(df)

# sqld 와 sqlp에 대한 평균점수 구하기
df['average'] = df['total'] / 2
# print(df)
grades = []
for row in df['average']:
    if row >= 60:
        grades.append('passed')
    else:
        grades.append('failed')

df['sql_result'] = grades
# print(df)

df = df[['name', 'adsp']]


def adspResult(row):
    if row >= 60:
        return 'pass'
    else:
        return 'fail'

df['result'] = ['' for _ in range(6)]
df.result = df.adsp.apply(adspResult)
# print(df)
df['acq_date'] = ['2022-01-26','2019-03-09','2018-09-17','2021-12-26','2022-10-21','2022-01-18']
# print(df)


def extract_year(row):
    return row.split('-')[0]

df['acq_year'] = df.acq_date.apply(extract_year)
# print(df)

# 데이터프레임에 데이터프레임 데이터 추가하기
df2 = pd.DataFrame([
        ['박은수', 70, 'pass', '2011-03-11', '2011']
   ],columns=['name', 'adsp', 'result', 'acq_date', 'acq_year']
)
# print(df2)
df = df.append(df2, ignore_index=True)
print(df)

