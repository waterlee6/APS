# 1197. 최소 스패닝 트리

'''
최소 스패닝 트리 : 주어진 그래프의 모든 정점을 연결하는 부분 그래프 중에서 가중치의 합이 최소인 트리
=> 최소 신장 트리
'''

# 두 노드의 부모 노드가 다르면 합치기
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


V, E = map(int, input().split())  # V: 정점의 개수, E: 간선의 개수
arr = []  # 각 간선과 가중치를 저장하기 위한 리스트
for _ in range(E):
    a, b, c = map(int, input().split())  # a번 정점, b번 정점, 가중치 c
    arr.append((c, a, b))  # 가중치, a번 정점, b번 정점

# 1. 가중치가 작은 순으로 정렬
arr.sort()
# print(f'arr : {arr}')

# 2. 유니온 파인드를 위한 parent 배열, union 함수, find 함수 만들기
parent = [x for x in range(V+1)]  # 노드 번호와 일치 위해 0번째는 비워둠
min_w = 0   # 가중치의 최솟값을 담을 변수
# print(f'원래 parent : {parent}')
i = 0

# 3. 순서대로 두 정점을 연결 -> union find
for edge in arr:
    w = edge[0]  # 두 노드 간의 가중치
    a = edge[1]  # 첫 번째 노드
    b = edge[2]  # 두 번째 노드
    i += 1

    # a와 b를 연결해서 사이클이 발생하지 않으면 연결하기
    if find(a) != find(b):
        union(a, b)
        min_w += w  # 이 때의 가중치 더하기
        # print(f'{i}번째 : {parent}')

print(min_w)
