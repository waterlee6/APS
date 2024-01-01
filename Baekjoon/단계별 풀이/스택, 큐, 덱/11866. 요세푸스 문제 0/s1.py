# 11866. 요세푸스 문제 0
'''
k번째 사람을 제거, 그 자리에서부터 다시 k번째 사람을 제거
1 2 3 4 5 6 7
1 2 x 4 5 6 7
1 2   4 5 x 7
1 x   4 5   7
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
ans = []

for i in range(1, N+1):
    arr.append(i)

i = 0
while arr:
    # print(arr)
    i += K-1
    # print('i : ', i)
    while i >= len(arr):
        i = i - len(arr)
    # print(f'{i}번째 빼기 : ', end='')
    ans.append(arr.pop(i))

print('<', end='')
print(*ans, sep=', ', end='')
print('>')
