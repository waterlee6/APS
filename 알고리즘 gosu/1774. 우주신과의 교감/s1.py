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
    x1, y1 = gods[a][0], gods[a][1]
    # b번 노드의 좌표
    x2, y2 = gods[b][0], gods[b][1]

    # 두 점 사이의 거리 구하기
    dis = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dis



N, M = map(int, input().split())  # N: 우주신들의 개수, M: 이미 연결된 신들과의 통로의 개수
gods = [()]  # 황선자와 우주신들의 좌표를 담을 리스트
for _ in range(N):
    gods.append(tuple(map(int, input().split())))

links = []  # 이미 연결된 통로를 담을 리스트
for _ in range(M):
    links.append(list(map(int, input().split())))

min_dis = 0  # 최소 길이를 담을 변수
# print(f'gods : {gods}')
# print(f'links : {links}')


# 1. parent 만들기(N개)
parent = [0] + [x for x in range(1, N+1)]  # 번호 일치 위해 0번 추가
# print(f'연결 전 parent : {parent}')

# 2. links의 이미 연결된 노드를 연결
for link in links:
    a = link[0]  # a번 노드
    b = link[1]  # b번 노드
    union(a, b)
    # 새로 만든 통로의 길이만 구하는 것!
    # min_dis += distance(a, b)  # 연결된 노드 간의 거리는 확정이므로 min_dis에 담아두기
# print(f'연결 후 parent : {parent}')
# print(f'처음 min_dis : {min_dis}')
# print('----------------------------------')

# 3. 아직 연결 안된 노드들을 거리 순으로 정렬하기 위한 탐색
yet_dis = []  # 아직 연결되지 않은 두 별 사이의 거리를 저장할 리스트 (가중치, a번 노드, b번 노드)
for i in range(1, N):
    for j in range(i+1, N+1):
        a, b = gods[i], gods[j]
        # 아직 연결이 안 되어 있으면 두 점 간의 길이를 구하기
        if find(i) != find(j):
            yet_dis.append((distance(i, j), i, j))   # 가중치, 노드 번호, 노드 번호
            # print(f'i, j : {i, j}')
            # print(f'yet_dis : {yet_dis}')

# 4. yet_dis 오름차순으로 정렬 (거리가 짧은게 먼저 나오게)
yet_dis.sort()
# print(f'sorted yet_dis : {yet_dis}')

# 5. 이 dis 함수에 대해서 union find 실행
for dis in yet_dis:
    w = dis[0]   # 가중치 = 두 노드 간의 거리
    i = dis[1]   # i번 노드 번호
    j = dis[2]   # j번 노드 번호
    # 사이클이 아니면 유니온 실행하고 min_dis에 더함
    if find(i) != find(j):
        union(i, j)
        min_dis += w

print(f'{min_dis:.2f}')
