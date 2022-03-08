def FindBalance(nums):
    print(nums)
    n = len(nums)
    if n == 1:
        return [0, nums[0], 0]
    f_sum = [0]
    tsum = 0
    for i in range(1, n):
        f_sum.append(f_sum[i - 1] + nums[i - 1])
    print(f_sum)
    for i in range(n - 2, 0, -1):
        tsum += nums[i + 1]
        print('tsum', tsum)
        if (tsum == f_sum[i]):
            return [i, nums[i], tsum]
    return []


print(FindBalance([1, 2, 3, 4, 5, 2, 3, 5]))