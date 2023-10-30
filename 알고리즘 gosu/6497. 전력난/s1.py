# 6497. 전력난

'''
도시의 모든 집을 방문할 수 있어야 함 -> 모든 노드가 연결되어 있어야 함
노드를 연결하는 길의 합이 최소가 되어야 함
=> 최소 신장 트리로 풀기


input 받는 것부터 잘 모르겠는데...

m, n = map(int, input().split())  # m: 집의 수, n: 길의 수
arr = []  # 노드 간의 거리를 저장할 리스트
while True:
    if tuple(map(int, input().split())) == (0, 0):
        break
    x, y, z = map(int, input().split())  # x: x번 노드, y: y번 노드, z: x와 y 사이의 거리
    print(x, y, z)
    # arr.append([z, x, y])
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


# distace 함수(두 점 사이의 거리)
import math
def distance(a, b):
    # a번 노드의 좌표
    x1, y1 = gods[a][0], gods[a][1]
    # b번 노드의 좌표
    x2, y2 = gods[b][0], gods[b][1]

    # 두 점 사이의 거리 구하기
    dis = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dis

# 1. input 받기
while True:
    m, n = map(int, input().split())  # m: 집의 수, n: 길의 수
    parent = [x for x in range(m+1)]

    if m == 0 and n == 0:
        break

    # 2. 두 노드(집)와 노드간 거리를 저장
    arr = [[]]   # 노드 간의 거리를 저장할 리스트 (집 번호와 일치 위해 [] 추가하고 시작)
    for i in range(n):
        x, y, z = map(int, input().split())  # x: x번 노드, y: y번 노드, z: x와 y 사이의 거리
        arr.append([z, x, y])
    # print(arr)     # [[], [7, 0, 1], [5, 0, 3], [8, 1, 2], [9, 1, 3], [7, 1, 4], [5, 2, 4], [15, 3, 4], [6, 3, 5], [8, 4, 5], [9, 4, 6], [11, 5, 6]]
    # print(parent)  # [0, 1, 2, 3, 4, 5, 6, 7]

    # 3. 거리가 짧은 순으로정렬
    arr.sort()

    # 4. 거리가 짧은 순으로 union find 수행
    for i in range(1, n+1):
        w = arr[i][0]   # w: 가중치
        x = arr[i][1]   # x: x 노드
        y = arr[i][2]   # y: y 노드

        # 사이클이 아니라면
        if
        


