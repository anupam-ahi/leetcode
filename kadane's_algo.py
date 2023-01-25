arr = []
_max = arr[0]
_sum = 0
for i in arr:
    _sum += i
    _max = max(_max, _sum)
    if _sum < 0:
        _sum = 0
print(_max)