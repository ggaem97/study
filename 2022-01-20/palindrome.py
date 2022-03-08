import sys
sys.stdin = open('b.txt', 'r')
n = int(input())
words = [input() for _ in range(n)]


def isPalindrome(word):
    start = 0
    end = len(word)-1
    while start <= end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True


def isPseudoPalindrome(word):
    n = len(word)
    s = ''
    for i in range(n):
        if i == 0:
            new_word = word[i+1:]
        elif i == n-1:
            new_word = word[:n-1]
        else:
            new_word = word[:i] + word[i+1:]

        if isPalindrome(new_word):
            return True
    return False


for w in words:
    if isPalindrome(w):
        print(0)
    elif isPseudoPalindrome(w):
        print(1)
    else:
        print(2)