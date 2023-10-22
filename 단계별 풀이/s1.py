# 2587. 대표값2

import statistics

arr = []
for _ in range(5):
    arr.append(int(input()))

avg = statistics.mean(arr)
med = statistics.median(arr)
print(avg)
print(med)