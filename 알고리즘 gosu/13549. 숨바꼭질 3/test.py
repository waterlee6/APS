# 13549. 숨바꼭질 3 (정답 코드로 돌려보기)

import sys

input = sys.stdin.readline
import heapq

a, b = map(int, input().split())
cut = abs(b - a)
visited = [100002 for i in range(200001)]
q = []
visited[b] = True
heapq.heappush(q, (0, b))

while True:
    # print(q)
    c, x = heapq.heappop(q)  # 최솟값 꺼냄!
    # print(c,x)
    # print()
    if x == a:
        print(c)
        break

    if c >= cut:
        print(cut)
        break

    if x % 2 == 0 and visited[x // 2] > c:
        visited[x // 2] = c
        heapq.heappush(q, (c, x // 2))
    if visited[x - 1] > c + 1:
        visited[x - 1] = c + 1
        heapq.heappush(q, (c + 1, x - 1))
    if visited[x + 1] > c + 1:
        visited[x + 1] = c + 1
        heapq.heappush(q, (c + 1, x + 1))
