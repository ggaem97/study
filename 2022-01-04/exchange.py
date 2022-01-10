n = 1250
count = 0
lst = [500, 100, 50, 10]
# for money in lst:
#     if n!=0:
#       count += n//money
#       n %= money
#     else:
#         break

for money in lst:
    count += n // money
    n %= money

# ZeroDivisionError
# print(2//0)
print(count)
