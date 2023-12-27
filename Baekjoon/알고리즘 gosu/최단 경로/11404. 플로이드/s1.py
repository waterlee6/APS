# 11404. 플로이드
'''
모든 도시의 쌍에 대해서 필요한 비용의 최솟값을 행렬로 출력
하나의 노드에서 나머지 노드로의 최단 경로를 구하는 것이 아닌
모든 노드에서 모든 노드로의 최단 경로를 구함 => 플로이드 워셜 알고리즘
시작 노드와 도착 노드를 연결하는 노선이 하나 이상 임에 주의!!!

>>플로이드 워셜 알고리즘<<
* distance와 q 필요 없음
* 2차원 행렬 형식의 routes에 비용을 바로 저장 <- ★routes를 inf로 초기화★
'''

import pprint
import sys
input = sys.stdin.readline

n = int(input())  # n: 도시의 개수
m = int(input())  # m: 간선의 개수
inf = 1e9         # 무한대를 상정

# 무한으로 초기화한 2차원 리스트에 버스 정보 입력
# 시작 노드와 도착 노드 사이에 간선이 하나 이상일 수 있음
# -> 이미 기존 값이 있을 때에는 더 작은 값으로 저장
routes = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    if routes[a][b] > w:
        routes[a][b] = w

# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            routes[i][j] = 0
# pprint.pprint(routes)

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):          # k: 중간 정점
    for a in range(1, n+1):      # a : 시작 정점
        for b in range(1, n+1):  # b: 종료 정점
            if a != b:
                routes[a][b] = min(routes[a][b], routes[a][k] + routes[k][b])

# 플로이드 워셜 알고리즘 수행 후 inf로 남아있는 경우(경로가 없는 경우)는 0으로 초기화
for i in range(n+1):
    for j in range(n+1):
        if routes[i][j] == inf:
            routes[i][j] = 0

# 정답 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        print(routes[i][j], end=' ')
    print()
