# 9370. 미확인 도착지
'''
s에서 출발해서 g-h를 반드시 지날 때, 최단거리로 도착할 수 있는 목적지 구하기
목적지를 새로 구하는 것이 아니라 주어진 후보 중에서 불가능한 경우 제외하기
주어진 경로를 지나는 최단거리가 아니라 무조건 최단거리이면서 주어진 경로도 지나야 함

힙큐를 사용한 다익스트라로 출발지 s에서 각 도착지 후보까지의 최단 거리 구하기
* s → g → h → end
* s → h → g → end

최단 경로를 구하는 것이 아니라 최단 경로일 때의 목적지를 구하는 것이므로, g-h의 길이를 구할 필요는 없음

모든 경로 저장할 때 양방향 그래프이므로 두 번 저장해 줘야 함

>> 다익스트라 함수 구현 <<
visited 리스트는 필요하지 않음
q(힙큐)와 최단 경로 테이블(distance) 필요
* q에는 탐색 중인 노드(now)에 연결되어 있는 특정 노드까지의 현재 기준 최단거리를 입력 (가중치, 연결 노드)
* 최단 경로 테이블(distance)에는 시작 노드(s) 부터 해당 노드까지 걸리는 최종적인 최단 경로를 입력
다익스트라 함수를 매번 실행하면 시간초과, 함수의 return 값으로 최단 경로 테이블이 나오도록 작성해 리스트를 변수에 저장해 두고 사용하기
'''

import heapq
import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')
inf = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 다익스트라 함수 만들기
def dijkstra(s):
    # 최단 경로 테이블을 무한으로 초기화하기
    distance = [inf] * (n + 1)
    q = []

    # 1. 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입, distance 0으로 설정
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:  # 큐가 비어있지 않다면
        # 2. 가중치가 가장 작은 노드를 큐에서 꺼내기
        dist, now = heapq.heappop(q)  # dist: 거리, now: 현재 탐색중인 노드

        # 3. 현재 노드가 이미 처리되었다면 무시
        # dist에는 now 노드까지 갈 수 있는 예상 최단거리가 기록되어 있음
        # 최단 경로 테이블에 이보다 작은 값이 기록되어 있다면 pass
        if distance[now] < dist:
            continue

        # 4. 현재 노드와 연결된 다른 인접한 노드들을 확인
        for route in routes[now]:
            cost = dist + route[1]  # cost: 새로운 최단거리 = 현재 탐색중인 노드까지의 최단거리 + 연결된 노드까지의 거리

            # 5. 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[route[0]]:  # 이 cost가 연결된 노드까지의 최단거리보다 짧으면
                distance[route[0]] = cost  # cost로 갱신
                heapq.heappush(q, (cost, route[0]))  # 큐에 삽입
    return distance


T = int(input())
for tc in range(T):
    n, m, e = map(int, input().split())  # n: 교차로 개수, m: 도로 개수, e: 목적지 후보 개수
    s, g, h = map(int, input().split())  # s: 출발지, g: 지나간 도로, h: 지나간 도로

    # 도로의 연결 정보를 담을 리스트에 간선 정보 담기
    # → 양방향이고 간선이 최대 하나 뿐이므로 리스트의 인덱스를 이용
    routes = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        routes[a].append((b, d))  # a 노드에서 b 노드로 가는 거리가 d
        routes[b].append((a, d))  # ★★★ 양방향이므로 b 노드에서 a 노드로 가는 거리도 입력

    # 목적지 후보룰 담을 리스트 만들기
    ends = []
    for _ in range(e):
        ends.append(int(input()))

    # 최종 정답을 담을 리스트 만들기
    ans = []

    # 목적지 별 다익스트라 함수 실행 -> 실행결과인 distance 리스트를 저장해 두기
    dijk_s = dijkstra(s)  # 출발지가 s인 다익스트라
    dijk_g = dijkstra(g)  # 출발지가 g인 다익스트라
    dijk_h = dijkstra(h)  # 출발지가 h인 다익스트라

    for end in ends:
        if dijk_s[g] + dijk_g[h] + dijk_h[end] == dijk_s[end] or dijk_s[h] + dijk_h[g] + dijk_g[end] == dijk_s[end]:
            ans.append(end)

    ans.sort()
    # print(f'{tc}번째 {ans}')
    print(*ans)
