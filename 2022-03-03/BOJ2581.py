import sys
import math
sys.stdin = open('2581', 'r')
n = int(input())
m = int(input())
primes = []
def isPrime(data):
    root = math.sqrt(data)
    if data == 1: return False
    for i in range(2, int(root) + 1):
        if num % i == 0:
            return False
    return True
for num in range(n, m+1):
    if isPrime(num):
        primes.append(num)
if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)