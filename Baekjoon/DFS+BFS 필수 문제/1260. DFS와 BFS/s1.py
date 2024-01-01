# 1260. DFS와 BFS

import sys
from pprint import pprint
input = sys.stdin.readline

N, M, V = map(int, (input().split()))  # N: 정점의 개수, M: 간선의 개수, V: 시작점
arr = [[0] * (N+1) for _ in range(N+1)]

# [인접행렬 만들기]
for _ in range(M):
    i, j = map(int, input().split())
    arr[i][j] = 1
    arr[j][i] = 1


## DFS ===================================================
# 1. stack, visited
stack = []
dfs_visited = [False] * (N+1)
i = V  # 시작점
dfs_route = [i]
dfs_visited[i] = True  # 시작점 방문표시

# 2. 탐색하기
while True:
    # 2-1. 현재 위치 i에서 탐색나갈 j가 있으면
    for j in range(1, N+1):
        if arr[i][j] == 1 and dfs_visited[j] == False:
            stack.append(i)      # 탐색 나갈 때 push
            # print('stack에 push : ', stack)
            dfs_route.append(j)  # route에 방문순서 표시

            i = j  # 탐색 중인 노드 바꾸기
            dfs_visited[i] = True
            break

    # 2-2. 현재 위치 i에서 더 이상 방문할 곳이 없으면
    else:
        if stack:
            i = stack.pop()
            # print('stack에 pop : ', stack)
        else:
            break

print(*dfs_route)


## BFS ===================================================
# 1. q, visited
q = []
bfs_visited = [False] * (N+1)
bfs_route = []
bfs_visited[V] = True  # 시작점 방문표시
q.append(V)            # 시작점 인큐

# 2. 탐색하기
while q:
    # 2-1. 디큐하기
    a = q.pop(0)  # 시작점
    bfs_route.append(a)

    # 2-2. 인큐하기
    for b in range(1, N+1):
        if arr[a][b] == 1 and bfs_visited[b] == False:
            q.append(b)
            bfs_visited[b] = True

print(*bfs_route)
