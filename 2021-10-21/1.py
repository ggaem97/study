import sys

f = open('in1.txt','r')

# readlines: 개행 포함
for line in f.readlines():
    print(line, end='')

f.close()

# 'w': 새로 쓰겠다는 의미
# f = open('in1.txt', 'w')
# 'a' : 원본 + 새로 쓸내용 추가
f = open('in1.txt', 'a')
f.write('Hello\nBye\n'+'Hello\nBye\n')
f.close()

f = open('in2.txt', 'w')
f = open('in3.txt', 'a')
f = open('test.txt','r')

f.close()


