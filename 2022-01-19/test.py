lst = [1,2,3,4,5]

lst.reverse()
print(lst)
lst.remove(3)
print(lst)
print(lst.count(4))
lst.append(2)
print(lst)
lst.remove(2)
print(lst)

sett = {5}
answer = [i for i in lst if i not in sett]
print(answer)

print('\'')
print('\"')
print('\\')

a = set([1,2,3,4,5])
b = set([5,5,5,4,4])
print(a|b)
print(a&b)
print(a-b)

a.add(8)
print(a)
a.update([55])
print(a)
a.remove(3)
print(a)
t = 5
print(f'정답은 {t}')
print('정답은 {}'.format(t))

print((lambda a,b:a+b)(2,5))
print((lambda x:x**2)(7))

arr = [('a',100),('b',80),('c',90)]
print(sorted(arr, key=lambda x:x[1], reverse=True))


aa = [1,2,3,4,5]
bb = [5,5,5,4,4]

lst = map(lambda a,b:a+b, aa,bb)
print(list(lst))

import heapq
from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement
print(list(combinations(aa, 2)))
print(list(permutations(aa,2)))
print(list(product(aa,repeat=2)))
print(list(combinations_with_replacement(aa, 2)))

from collections import deque
import math


answer = eval("2+2*3")
print(answer)


from collections import Counter

counter = Counter(['red','blue','purple','gray','red'])
print(counter['red'])
print(dict(counter))

import math

a = 24
b = 8


def lcm(a,b):
    return a*b//math.gcd(a,b)


print(math.gcd(a,b))
print(lcm(a,b))


def gcd(a,b):
    if a<b:
        gcd(b,a)
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

print('?',gcd(48,6))
print(gcd(6,70))
