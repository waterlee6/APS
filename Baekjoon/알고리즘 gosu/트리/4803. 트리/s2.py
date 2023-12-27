# 4803. 트리

def bfs(i, arr):  # i: 현재 탐색중인 정점, arr: 인접행렬
    global Tree, visited

    # 1. Q, 시작점 인큐
    Q = []
    Q.append(i)

    # 2. BFS 탐색
    while Q:  # Q가 남아있는 동안

        # 2-1. 디큐하기(탐색하기) + ★디큐할 때 visited
        i = Q.pop(0)
        if visited[i] == 0:
            visited[i] = 1
        else:
            Tree = False
            # break  # ...(2)

        # 2-2. 인큐하기
        for j in range(1, n + 1):
            if arr[i][j] == 1 and visited[j] == 0:  # i와 j 노드가 연결되어 있고, j노드를 방문 전이면
                Q.append(j)


tc = 0  # 테스트 케이스의 번호를 셀 변수
while True:
    n, m = map(int, input().split())  # n: 정점의 개수, m: 간선의 개수
    tc += 1
    T = 0  # 트리의 개수를 셀 변수

    if n == 0 and m == 0:
        break  # while문 탈출
    else:
        # 1. 인접행렬 만들기
        arr = [[0] * (n + 1) for _ in range(n + 1)]
        for _ in range(m):
            v1, v2 = map(int, input().split())
            arr[v1][v2] = 1
            arr[v2][v1] = 1

        # 2. visited 만들기
        visited = [0] * (n + 1)

        # 3. 주어진 그래프를 bfs 함수로 탐색 -> 트리가 맞다면 T += 1
        # 시작노드 i를 뭘로 설정?
        # 주어진 모든 노드에 대해 탐색해야 함 -> visited[i]가 아직 미탐색이면 bfs
        for i in range(1, n + 1):  # 전체 노드의 개수
            Tree = True            # 순회인지 아닌지를 판단할 변수(매 i마다 초기화) ...(1)
            if visited[i] == 0:
                bfs(i, arr)        # 아직 방문하지 않은 노드면 bfs 탐색을 돌림
                if Tree:           # Tree 값이 True이면 트리가 맞으므로
                    T += 1         # T에 1을 더함

        # 4. 출력하기
        # 여기서 Tree == False 인 걸로 판단하면 False, False, True인 경우 True 개수가 세짐
        if T == 0:
            print(f'Case {tc}: No trees.')
        elif T == 1:
            print(f'Case {tc}: There is one tree.')
        else:
            print(f'Case {tc}: A forest of {T} trees.')
