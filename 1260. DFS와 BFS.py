# 1260. DFS와 BFS

V, E, N = map(int, input().split()) # V: 정점의 개수, E: 간선의 개수, N: 탐색을 시작할 정점의 번호
data = []
for _ in range(E):
    data.extend(list(map(int, input().split())))


# DFS --------------------------------------------------
dfs_route = []
# [인접행렬]
arr = [[0] * (V+1) for _ in range(V+1)]  # 노드 번호와 일치시키기 위해 +1
for i in range(E):  # 간선 정보를 채우는 것이므로 E
    ni, nj = data[i*2], data[i*2+1]
    arr[ni][nj] = 1  # 연결표시
    arr[nj][ni] = 1  # 양방향이 아니라면 한 번만

# [DFS 함수]
def dfs(i) :  # i: 현재 탐색 중인 정점
    global dfs_route

    # 1. visited, stack, route
    visited = [0] * (V+1)
    stack = []
    visited[i] = 1  # 현재 탐색 중인 정점에 방문 표시
    dfs_route = [i]     # 탐색 경로를 저장할 리스트, i를 저장하고 시작

    # 2. dfs 탐색 시작(for else 구문)
    while True:
        # 2-1. 현재 위치 i에서 탐색나갈 j가 있으면
        for j in range(1, V+1):
            if arr[i][j] == 1 and visited[j] == 0:  # i와 j가 연결되어 있고 아직 미방문이면
                dfs_route.append(j)   # ★탐색경로를 표시(j)
                stack.append(i)   # ★stack에 push(i) -> stack에는 탐색 나갈 때 push

                i = j  # 현재 탐색 중인 노드의 위치 바꾸기
                visited[i] = 1    # 방문 표시
                break  # for문에서 break

        # 2-2. 현재 위치 i에서 더 이상 방문할 곳이 없으면 -> 뒷걸음질
        else:
            if stack:  # stack에 정점이 남아있으면 -> 뒷걸음질 칠 자리가 있음
                i = stack.pop()
            else:      # stack이 비어있으면 -> 뒷걸음질 칠 자리가 없음
                break  # while문에서 break


# BFS --------------------------------------------------
# [인접행렬]
bfs_route = []  # 탐색 경로를 저장할 리스트
arr2 = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    ni, nj = data[2*i], data[2*i+1]
    arr2[ni][nj] = 1
    arr2[nj][ni] = 1

# [BFS 함수]
def bfs(i):  # i: 현재 탐색 중인 정점
    global bfs_route

    # 1. visited, Q, 시작점 인큐, 시작점 visited
    visited = [0] * (V+1)
    Q = []
    Q.append(i)
    bfs_route.append(i)  # 인큐할 때 저장하므로 경로도 저장하고 시작
    visited[i] = 1
    
    # 2. BFS 탐색 시작
    while Q:  # Q가 남아있는 동안

        # 2-1. 디큐하기 ★ 탐색하기
        front = Q.pop(0)
        
        # 2-2. 인큐하기
        for i in range(1, V+1):
            if arr2[front][i] == 1 and visited[i] == 0:  # front 노드와 i노드가 연결되어 있고 아직 방문 전이면
                Q.append(i)     # 인큐하기
                visited[i] = visited[front] + 1  # visited 처리(거리까지 표시하는 visited)
                bfs_route.append(i)


dfs(N)
print(*dfs_route)
bfs(N)
print(*bfs_route)