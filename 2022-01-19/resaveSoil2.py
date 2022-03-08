N, L = 3, 3
# pools= sorted(tuple(map(int, input().split())) for i in range(N))
pools = [(1,6),(8,12),(13,17)]
res, s = 0, 0
for start, end in pools:
  s = max(start, s)
  print('s',s)
  diff = end - s
  count = (diff + L - 1) // L
  # print(diff)
  print(count)
  res += count
  s += count * L

print(res)