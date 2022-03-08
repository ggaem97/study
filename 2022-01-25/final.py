import pandas as pd

customer = [
    {'name': '한정민', 'age': 26, 'address': 'Ansan', 'account':85000000},
    {'name': '박우혁', 'age': 29, 'address': 'Soowon', 'account':95211001},
    {'name': '김설준', 'age': 25, 'address': 'Dokyo', 'account':151000215},
    {'name': '존리', 'age': 58, 'address': 'Bucheon', 'account':5554422100},
    {'name': '최인수', 'age': 30, 'address': 'Incheon', 'account':52200005},
    {'name': '유재석', 'age': 45, 'address': 'Seoul', 'account':88112155500}
]
df = pd.DataFrame(customer, columns=['name', 'age', 'address', 'account'])
# print(df)
# print()
# 인덱스 번호 2번째부터 출력
# print(df.iloc[2:])
# print()
# print(df['name'])
# df.to_csv('customer.csv')

# 나이가 50이상인 row만 출력
# print(df[df.age>=50])
# print(df.query('age'>=50)) 땡!
# print(df.query('age>=50'))

# 나이가 29살이면서 수원에 사는 사람 구하기
# print(df[(df.age == 29) & (df.address == 'Soowon')])
# print(df.query("(address == 'Soowon') and (age == 29)"))

# 원하는 컬럼만 떼어서 붙이기

# 컬럼 이름 바꾸기
# df.columns[[1,2,3,4]]  땡!

# df.columns = [1,2,3,4]
# print(df)


# 두개의 1차원 자료구조인 시리즈 합쳐 데이터 프레임 만들기
# s1 = pd.Series([1,2,3])
# s2 = pd.Series(['one', 'two', 'three'])

# df2 = pd.DataFrame(dict(num=s1, word=s2))
# print(df2)

# csv 파일로 저장하기
# df.to_csv('customer.csv')

# df.to_csv('customer.csv', header=False, index=False)
# 한정민,26,Ansan,85000000
# 박우혁,29,Soowon,95211001
# 김설준,25,Dokyo,151000215
# 존리,58,Bucheon,5554422100
# 최인수,30,Incheon,52200005
# 유재석,45,Seoul,88112155500

# csv 데이터 파일 가져오기
# df3 = pd.read_csv('hello.csv')

# 헤더 없는 csv 데이터 파일 가져오면서 헤더 추가하기
# df3 = pd.read_csv('hello.csv', names=['num', 'word'])
# print(df3)


# df.to_csv('customer.csv', index=False, header=True)
# tab으로 구분된 테이블 파일 가져오기

# df3 = pd.read_csv('customer.csv', delimiter='\t')
# print(df3)
# df4 = pd.read_csv('customer.txt', delimiter='\t')
# print(df4)

# null 값을 '없음'으로 처리하여 저장하기
# print(df)
# customer = [
#     {'name': '한정민', 'age': 26, 'address': 'Ansan', 'account':85000000},
#     {'name': '박우혁', 'age': 29, 'address': 'Soowon', 'account':95211001},
#     {'name': '김설준', 'age': 25, 'address': 'Dokyo', 'account':151000215},
#     {'name': '존리', 'age': 58, 'address': 'Bucheon', 'account':5554422100},
#     {'name': '최인수', 'age': 30, 'address': '', 'account':52200005},
#     {'name': '유재석', 'age': 45, 'address': 'Seoul', 'account':88112155500}
# ]
# df = pd.DataFrame(customer)
# df.to_csv('customer.csv', index=False, header=False, na_rep='-')

# 최상단 두개의 행만 가져오기
# print(df.head(2))

# print(df)
# 컬럼 위치 바꾸기  ... (1)
# print(df)
# df.columns = ['name', 'account', 'address', 'age']
# df = df[['name', 'account', 'address', 'age']]
# print(df)

# 리스트 내 딕셔너리로 데이터프레임 만들때 column의 순서는 보장되지 못함
# (1)의 방식으로 컬럼 지정하거나
# collections 라이브러리의 OrderDict 모듈을 활용하면 해결 가능
# from collections import OrderedDict
# ordered_customer = OrderedDict(
#     [
#         ('name', ['한정민', '박우혁', '김설준', '존리', '최인수', '유재석']),
#         ('age', [26, 29, 25, 58, 30, 45]),
#         ('address', ['Ansan', 'Soowon', 'Dokyo', 'Bucheon', 'Incheon', 'Seoul']),
#         ('account', [85000000, 95211001, 151000215, 5554422100, 52200005, 88112155500])
#     ]
# )
# df2 = pd.DataFrame.from_dict(ordered_customer)
# print(df2)

# print(df)
# df.index = ['zero','one', 'two', 'three', 'four', 'five']
# print(df)

# 인덱스로 로우 데이터 확인
# print(df.loc[''])
# 행번호로 로우 데이터 확인
# print(df.iloc[1])

customer_record = [
    ['한정민', 26, 'Ansan', 85000000],
    ['박우혁', 29, 'Soowon', 95211001],
    ['김설준', 25, 'Dokyo', 151000215],
    ['존리', 58, 'Bucheon', 5554422100],
    ['최인수', 30, 'Incheon', 52200005],
    ['유재석', 45, 'Seoul', 88112155500]
]

# df2 = pd.DataFrame.from_records(customer_record)
# print(df2)

# 2,3 번째 컬럼, 0,1 번째 로우만 가져오기
# df.index = [0,1,2,3,4,5]
# print(df.iloc[:2, 2:4])

# 컬럼명을 가지고 필터링하기
# df.columns = ['name', 'age', 'address', 'account']
# print(df[['name','account']])
# print(df.filter(['name','account']))
print(df.drop([1, 3]))