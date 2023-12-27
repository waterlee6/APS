# 1504. 특정한 최단 경로
'''
두 노드 간의 간선은 방향성이 없음(양방향) -> 간선 정보를 저장할 때 양방향으로 저장해야 함!!
1번 정점에서 V번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동
조건을 만족하는 간선이 존재하지 않을 때를 고려해야 함
반드시 v1을 먼저 방문하고 v2를 방문한다고 볼 수는 없지 않나?
distance와 visited를 매번 초기화하는 이유? 지나온 간선/노드를 재방문해도 상관 X, 무조건 최단거리로만 이동하면 되므로
'''

# 아직 방문하지 않은 노드 중, 최단 경로가 가장 짧은 노드를 찾기
def find_next_node():
    shortest = inf
    index = 0
    for v in range(1, V+1):
        if visited[v] == False and distance[v] < shortest:
            shortest = distance[v]
            index = v
    return index


# 다익스트라 알고리즘을 실행하는 함수
def dijkstra(start):  # start : 시작 노드
    # 1. 시작 노드 표시하기
    distance[start] = 0  # 자기 자신은 0으로 표시
    visited[start] = True  # 방문 표시

    # 2. 시작 노드와 연결되어 있는 노드들을 distance에 표시
    for link in links[start]:
        distance[link[0]] = link[1]

    # 3. 시작 노드를 제외한 나머지 노드들에서 탐색
    for i in range(V-1):

        # 3-1. distance에서 값이 가장 작은 노드를 찾기
        new = find_next_node()
        visited[new] = True  # 방문표시

        # 3-2. new와 연결된 다른 노드들을 확인
        for link in links[new]:
            if distance[link[0]] > distance[new] + link[1]:
                distance[link[0]] = distance[new] + link[1]


import sys
input = sys.stdin.readline
V, E = map(int, input().split())
links = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    links[a].append([b, c])  # a번 정점에서 b번 정점으로 이동하는 거리가 c
    links[b].append([a, c])  # b번 정점에서 a번 정점으로 이동하는 거리가 c
v1, v2 = map(int, input().split())
inf = sys.maxsize  # 재형이꺼 보고 베껴봄...


# 1. 1 -> v1 -> v2 -> V 경우
# distance와 visited 초기화
distance = [inf] * (V+1)
visited = [False] * (V+1)
dijkstra(1)
rst1 = distance[v1]

distance = [inf] * (V+1)
visited = [False] * (V+1)
dijkstra(v1)
rst2 = distance[v2]

distance = [inf] * (V+1)
visited = [False] * (V+1)
dijkstra(v2)
rst3 = distance[V]

ans1 = rst1 + rst2 + rst3
if ans1 >= inf:
    ans1 = -1

# 2. 1 -> v2 -> v1 -> V 경우
distance = [inf] * (V+1)
visited = [False] * (V+1)
dijkstra(1)
rst1 = distance[v2]

distance = [inf] * (V+1)
visited = [False] * (V+1)
dijkstra(v2)
rst2 = distance[v1]

distance = [inf] * (V+1)
visited = [False] * (V+1)
dijkstra(v1)
rst3 = distance[V]

ans2 = rst1 + rst2 + rst3
if ans2 >= inf:
    ans2 = -1

print(min(ans1, ans2))