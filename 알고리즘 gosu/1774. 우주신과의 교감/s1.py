# 1774. 우주신과의 교감

'''
통로들의 길이 : 2차원 좌표계상의 거리
아직 연결되지 않은 노드와 연결하기 -> 길이의 합이 최소가 되도록
황선자의 위치가 어딘지는 몰라도 됨 -> 어차피 다 연결할 것이므로
'''
# find 함수
def find(a):
    # [종료조건]
    if parent[a] == a:
        return a
    # [수행내용]
    parent[a] = find(parent[a])
    return parent[a]


# union 함수
def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a < root_b:
        parent[root_b] = root_a
    elif root_a > root_b:
        parent[root_a] = root_b

import math

# distace 함수(두 점 사이의 거리)
def distance(a, b):
    # a번 노드의 좌표
    x1, y1 = locations[a][0], locations[a][1]
    # b번 노드의 좌표
    x2, y2 = locations[b][0], locations[b][1]

    # 두 점 사이의 거리 구하기
    dis = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dis



N, M = map(int, input().split())  # N: 우주신들의 개수, M: 이미 연결된 신들과의 통로의 개수
locations = [()]  # 황선자와 우주신들의 좌표를 담을 리스트
for _ in range(N):
    locations.append(tuple(map(int, input().split())))

links = []
for _ in range(M):
    links.append(list(map(int, input().split())))

min_dis = 0  # 최소 길이를 담을 변수
# print(locations)   # [(), (1, 1), (3, 1), (2, 3), (4, 3)]
# print(links)  # [[1, 4]]


# parent 만들기(N개)
parent = [0] + [x for x in range(1, N+1)]  # 번호 일치 위해 0번 추가
print(f'연결 전 parent : {parent}')

# links의 이미 연결된 노드를 연결
for link in links:
    a = link[0]  # a번 노드
    b = link[1]  # b번 노드
    union(a, b)
    min_dis += distance(a, b)  # 연결된 노드 간의 거리는 확정이므로 min_dis에 담아두기

print(f'연결 후 parent : {parent}')
print(min_dis)

# 그다음에 이제 아직 연결 안된 애들을 연결해야 하는데...
# 모든 경우의 수를 다 탐색?
for i