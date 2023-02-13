from collections import Counter
count = 0
_map = {}
arr = [1, 5, 7, 1]
k = 6

_map = Counter(arr)
count = 0
for i in arr:
    comp = k - i
    if comp in _map:
        count += _map[comp]
    if comp == i:
        count -= 1

print(int(count // 2))
