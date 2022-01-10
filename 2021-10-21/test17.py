# import os
# 절대경로 출력
# print(os.getcwd())

# r: 존재하는 파일 읽기
fH = open('C:/Users/dkwlw/PycharmProjects/swProject/04/04/test17.dat', 'r')
lines = fH.readlines()
# print(lines)
# ['Good Morning\n', 'How are you\n', 'Nice to meet you\n', 'Bye\n']
fH.close()

# w : 새로운 파일 생성하기
fH = open('test17.txt', 'w')

for line in lines:
    words = line.split(' ')
    # print(words)
    # ['Good', 'Morning\n']
    # ['How', 'are', 'you\n']
    # ['Nice', 'to', 'meet', 'you\n']
    # ['Bye\n']

    # '구분자'.join(리스트) > 리스트 원소들 문자열로 합치기
    # fH.write(' '.join(words) + '\n')
    fH.write(words[0] + '\n')
fH.close()

fH = open('a.txt','r')
d = []
for line in fH:
    # d = line.split()
    d += line.split()
print(d)
p = list(line.split() for line in fH)
print(p)

fH.close()
