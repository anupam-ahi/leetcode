intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals.sort(key=lambda i: i[0])
final = [intervals[0]]

for start, end in intervals[1:]:
    lastEnd = final[-1][1]
    if start <= lastEnd:
        final[-1][1] = max(end, lastEnd)
    else:
        final.append([start, end])
print(final)
