import sys
sys.stdin = open('switch.txt','r')

n = int(input())
b = input()
target = input()


def switch(bulb, x):
    global  target
    if x == 0:
        new_bulb = bulb
        # 비트 반전시키기

    elif x == len(bulb)-1:
        new_bulb = bulb
        # 비트 반전 시키기
    else:
        new_bulb = bulb
        # 비트 반전 시키기
    if new_bulb == target:
        return True
    if x == len(bulb)-1:
        return False
    switch(new_bulb, x + 1)


# switch('000', 0)
print(~0)
print(~1)