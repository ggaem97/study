a = 3
b = 16

while a<=b:
    if a in (2,3,5):
        print(a)
    elif a%2==0 or a%3==0 or a%5==0:
        pass
    else:
        print(a)
    a += 1