# 1753. 최단경로
'''
주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하기 -> 다익스트라 알고리즘
반례 : 같은 두 정점에 대해 여러 개의 간선이 존재할 수 있음
'''


# 아직 방문하지 않은 노드 중, 최단 경로가 가장 짧은 노드를 찾기
def find_next_node():
    shortest = inf  # 최단 경로
    index = 0  # 최단 경로 노드의 인덱스
    for v in range(1, V+1):
        if visited[v] == False and distance[v] < shortest:
            shortest = distance[v]
            index = v
    return index


def dijkstra(k):  # k: 시작 정점의 번호
    # 1. 시작 노드 표시하기
    distance[k] = 0     # 자기자신과의 거리는 0으로 표시
    visited[k] = True   # k번째 노드 방문 표시

    # 1-1. k번 노드와 연결되어 있는 노드들의 거리를 distance에 갱신
    for link in links[k]:
        # ★★★ 두 노드 사이에 간선이 여러 개 있을 수 있으므로 첫번째 노드에서도 거리 비교 해줘야 할 듯
        if distance[link[0]] == inf:
            distance[link[0]] = link[1]
            # distance[link[0]] = distance[k] + link[1]   # 이 코드도 상관 없겠지?
        else:
            if distance[link[0]] > link[1]:
                distance[link[0]] = link[1]

    # 2. ★★★ 시작 노드를 제외한 나머지 노드들에서 탐색
    for i in range(V-1):  # 시작 노드를 제외하고 남은 V-1번 탐색 수행

        # 2-1. distance에서 가장 가까운 노드(값이 가장 작은)를 찾기
        new = find_next_node()
        visited[new] = True  # 방문 표시

        # 2-2. new와 연결된 다른 노드들을 확인
        for link in links[new]:
            # v번 노드로 가는 기존 경로보다 새로운 경로가 더 가까우면
            # 새로운 경로 : 현재 노드 u까지 오는 길 + 현재 노드 u에서 v로 가는 길(가중치 w)
            if distance[link[0]] > distance[new] + link[1]:
                distance[link[0]] = distance[new] + link[1]


import sys
input = sys.stdin.readline
V, E = map(int, input().split())  # V: 정점의 개수, E: 간선의 개수
k = int(input())    # K: 시작 정점의 번호
inf = 30000000      # 최단 경로
links = [[] for _ in range(V+1)]  # 간선 연결 정보를 담을 리스트 / [n]으로 n번 노드와 연결된 링크를 한 번에 알 수 있도록
for _ in range(E):
    u, v, w = map(int, input().split())
    links[u].append([v, w])  # u번 노드에서 v번 노드로 가는 경로가 w라는 뜻

# 최단 경로 테이블, visited 만들기 (노드 번호와 일치시키기 위해 0번 인덱스는 비워둠)
distance = [inf] * (V+1)
visited = [False] * (V+1)

# 다익스트라 알고리즘 수행
dijkstra(k)

for d in distance[1:]:  # 0번 인덱스는 자리 맞추기용 이므로 제외하고
    if d == inf:
        print('INF')
    else:
        print(d)