# 28279. 덱 2

import sys
input = sys.stdin.readline
from collections import deque
q = deque()

N = int(input())
for _ in range(N):
    orders = input().split()
    order = orders[0]

    if order == '1':
        q.appendleft(int(orders[1]))
    elif order == '2':
        q.append(int(orders[1]))
    elif order == '3':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif order == '4':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif order == '5':
        print(len(q))
    elif order == '6':
        if q:
            print(0)
        else:
            print(1)
    elif order == '7':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order == '8':
        if q:
            print(q[-1])
        else:
            print(-1)
