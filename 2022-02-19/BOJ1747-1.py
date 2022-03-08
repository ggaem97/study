from math import sqrt
import sys
sys.stdin = open('1747.txt', 'r')


def isPrime(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def isPalindrome(num):
    data = str(num)
    k = len(data)
    for i in range(k//2):
        if data[i] != data[k-1-i]:
            return False
    return True


n = int(input())
while True:
    if isPrime(n):
        if isPalindrome(n):
            print(n)
            break
    n += 1
