# 10773. 제로

import sys
input = sys.stdin.readline

K = int(input())
arr = []
for k in range(K):
    num = int(input())

    # k가 0이 아니면 해당 수를 쓰기
    if num != 0:
        arr.append(num)

    # k가 0이면 가장 최근 수를 지우기
    else:
        arr.pop()

ans = sum(arr)
print(ans)
