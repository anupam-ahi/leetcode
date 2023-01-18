list1 = [4, 5, 1, 2]
first, last = 0, len(list1) - 1

while first < last:
    list1[first], list1[last] = list1[last], list1[first]
    first += 1
    last -= 1
print(list1)
    
