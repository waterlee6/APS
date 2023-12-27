# 4386. 별자리 만들기

'''
최소 비용 신장 트리
비용 : 두 별 사이의 거리 -> 거리 계산 필요
모든 점을 연결했을 때 가장 가까운 거리 구하기

간선별 가중치가 미리 주어지지 않음 -> 가중치 오름차순으로 정렬하고 시작 불가능
어느 점과 어느 점을 연결할지 어떻게 알지?
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
stars = []  # 별의 위치를 담을 리스트

for _ in range(N):
    stars.append(tuple(map(float, input().split())))
print(f'원래 stars : {stars}')  # [(1.0, 1.0), (2.0, 2.0), (2.0, 4.0)]
parent = [i for i in range(N)]
print(f'원래 parent : {parent}')  # [0, 1, 2]
min_cost = 0   # 최소 비용을 담을 변수
print()

# 1. arr의 첫 번째 원소부터 다음 원소 간의 거리를 탐색해서 가장 가까운 애랑 먼저 연결하기?
# => 이렇게 짜면 앞의 원소들은 최소 하나의 노드와는 무조건 연결되게 됨
# 연결이 안 되는 경우도 있읕텐데
for n in range(N):  # n: stars의 인덱스
    print(f'{n}번째 원소를 어디에 연결하지?')
    local_min_cost = 2000  # 거리의 최솟값은 다음 n으로 넘어갈 때 초기화

    for m in range(N):  # m: starst의 인덱스
        if n == m or find(n) == find(m):  # n == m이면 같은 노드이므로 pass
            continue                      # fins(n) == find(m)이면 사이클이므로 pass

        else:
            temp_cost = distance(stars[n], stars[m])
            print(f'{n}노드-{m}노드 사이 거리 : {temp_cost:.2f}')
            if temp_cost < local_min_cost:
                local_min_cost = temp_cost
                idx = m
                print(f'local 갱신! {idx}번째 노드와 연결, {local_min_cost:.2f}')
    
    # 2. m을 한 바퀴 다 돌고 나서 현재의 local_min_cost, idx 값으로 union 진행
    union(n, idx)
    min_cost += local_min_cost
#
    print(f'{n}과 {idx}를 연결한 parent : {parent}')
    print(f'local_min_cost : {local_min_cost:.2f}')
    print()
# ans = f'{min_cost:.2f}'
# print(ans)
