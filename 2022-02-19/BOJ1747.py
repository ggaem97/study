import sys

sys.stdin = open('1747.txt', 'r')


def isPrime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def isPalindrome(num):
    data = str(num)
    return data == data[::-1]


n = int(input())
while True:
    if isPrime(n):
        if isPalindrome(n):
            print(n)
            break
    n += 1
