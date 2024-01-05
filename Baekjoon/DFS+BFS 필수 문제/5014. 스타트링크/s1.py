# 5014.스타트링크

import sys
input = sys.stdin.readline
from collections import deque

F, S, G, U, D = map(int, input().split()) # 총 F층, S에서 G층으로 이동, 위로 U층 이동, 아래로 D층 이동

q = deque()
q.append(S)     # 시작점 인큐
visited = [-1] * (F+1)
visited[S] = 0  # 시작점 visited

if S == G:
    print(0)

else:
    while q:
        # 디큐하기
        i = q.popleft()
        # print(f'{i}번째 노드를 탐색')

        # 종료조건
        if i == G:
            # print('종료함')
            break

        # 인큐하기
        for j in [i+U, i-D]:
            if 1 <= j <= F and visited[j] == -1:
                q.append(j)
                visited[j] = visited[i] + 1
                # print(visited)

    if visited[G] == -1:
        print('use the stairs')
    else:
        print(visited[G])