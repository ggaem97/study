# s = list('1234')
s = list(input())
s.sort(key=lambda x:-int(x))
print(''.join(s))