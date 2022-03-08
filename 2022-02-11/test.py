from collections import deque
answer = [i for i in reversed(range(6))]
print(answer)

deq = deque(answer)
print(deq)
deq.reverse()
print(deq)

d = dict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d)
print(d.get('a'))
print(max(d, key=d.get))