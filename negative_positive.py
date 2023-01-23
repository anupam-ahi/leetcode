arr = [ -1, 2, -3, 4, 5, 6, -7, 8, 9]

i, j = -1, 0
while j < len(arr):
    if arr[j] < 0:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
    j += 1
print(arr)