# 4386. 별자리 만들기

'''
최소 비용 신장 트리
비용 : 두 별 사이의 거리 -> 거리 계산 필요
모든 점을 연결했을 때 가장 가까운 거리 구하기

간선별 가중치가 미리 주어지지 않음 -> 가중치 오름차순으로 정렬하고 시작 불가능
어느 점과 어느 점을 연결할지 어떻게 알지?

다른 MST와 input이 달라서 어려움 -> input을 똑같이 만들어놓고 시작하자!
'''

import math


# 두 점의 좌표가 주어졌을 때 거리를 구하는 함수
def distance(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dis


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    # 사이클 발생시 pass
    if root_a < root_b:
        parent[root_b] = root_a
    elif root_a > root_b:
        parent[root_a] = root_b


def find(a):
    # [종료조건]
    if a == parent[a]:
        return a
    # [수행내용]
    parent[a] = find(parent[a])
    return parent[a]



N = int(input())  # N: 별의 개수
stars = []  # input을 담을 리스트
links = []  # 별 연결과 가중치를 담을 리스트
min_cost = 0  # 최소 비용을 담을 변수
parent = [i for i in range(N)]

for _ in range(N):
    stars.append(tuple(map(float, input().split())))

# 1. 두 별 사이의 거리를 가중치로 해서 (가중치, 점 A, 점 B) 순서의 리스트 만들기
    # 주어진 점 N개에 대해서  모든 경우의 수를 다 계산?
    # -> 최대 경우의 수는 100C2 = 4950개이므로 계산 가능
    # 별의 좌표를 리스트에 넣는 것이 아니라 stars의 인덱스로 넣어서 찾기

visited = []  # 중복 제거에 사용할 visited
for a in range(N):  # 점 A
    for b in range(N):  # 점 B
        if a == b:  # 자기자신과는 연결하지 않음
            continue
        if (b, a) in visited:  # 중복 제거? a -> b 갔으면 b -> a 안가도록?
            continue
        else:
            # print(a, b)
            # 점 A(x1, y1), 점 B(x2, y2) 좌표 구하기
            A = (stars[a][0], stars[a][1])
            B = (stars[b][0], stars[b][1])

            # 두 점 사이의 거리 구하기
            dis = distance(A, B)

            # stars 리스트에 값을 저장하기
            links.append((dis, a, b))
            visited.append((a, b))
            # print(visited)
            # print([dis, a, b])


# 2. arr를 가중치 오름차순으로 정렬
links.sort()

# 3. 순서대로 두 정점을 연결
for link in links:
    w = link[0]  # 가중치
    a = link[1]  # 첫 번째 별의 좌표
    b = link[2]  # 두 번째 별의 좌표

    # 3-1. 사이클이 발생하지 않으면
    if find(a) != find(b):
        union(a, b)
        min_cost += w

print(f'{min_cost:.2f}')
