def bfs(i, arr):  # i: 현재 탐색중인 정점, arr: 인접행렬
    global Tree, visited

    # 1. Q, 시작점 인큐
    Q = []
    Q.append(i)

    # 2. BFS 탐색
    while Q:  # Q가 남아있는 동안

        # 2-1. 디큐하기(탐색하기) + visited하기
        i = Q.pop(0)
        if visited[i] == 0:
            visited[i] = 1  # ★디큐할 때 visited
            # print(i)
        else:
            Tree = False
            break  # visited에 이미 표시되어 있으면 순회이므로 Tree를 체크하고 while문 break

        # 2-2. 인큐하기
        for j in range(1, n + 1):
            if arr[i][j] == 1 and visited[j] == 0:  # i와 j 노드가 연결되어 있고, j노드를 방문 전이면
                Q.append(j)
                print(j)

n, m = map(int, input().split())  # n: 정점의 개수, m: 간선의 개수
visited = [0] * (n + 1)
arr = [[0] * (n + 1) for _ in range(n + 1)]  # 인접행렬을 기록할 빈 행렬
for _ in range(m):
    v1, v2 = map(int, input().split())
    arr[v1][v2] = 1
    arr[v2][v1] = 1

bfs(1, arr)