# 20040. 사이클 게임

'''
find 함수와 union 함수는 1717과 동일하게 사용
매 턴마다 선분을 하나씩 추가
사이클이 있는지 탐색
사이클이 생겼으면 -> i(번째)를 출력
끝까지 사이클이 생기지 않으면 -> 0을 출력
사이클이 생겼는지는 어떻게 알지? -> 경로압축을 해서 parent에 root node가 나오도록
'''


# 1. find 함수 만들기
def find(a):
    # [종료조건]
    if parent[a] == a:
        return a
    # [수행내용]
    parent[a] = find(parent[a])  # 경로압축이 일어나는 부분
    return parent[a]


# 2. union 함수 만들기
def union(a, b):
    a_root = find(a)
    b_root = find(b)
    # a와 b의 루트를 비교해서 더 작은 쪽으로 합치기
    if a_root > b_root:
        parent[a_root] = b_root
    elif a_root < b_root:
        parent[b_root] = a_root
    # 두 루트노드가 같다면 이미 합집합이므로 union 필요 없음


import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n: 점의 개수, m: 진행된 턴 수
turns = [[0, 0]] + [list(map(int, input().split())) for _ in range(m)]  # i와 맞추기 위해 [0, 0] 추가
rst = 0  # 사이클 결과를 출력할 변수
parent = [x for x in range(n)]

# 3. 턴을 진행하며 선분을 연결하기
for i in range(1, m + 1):
    # 3-1. 연결할 두 노드를 찾기
    a = turns[i][0]
    b = turns[i][1]

    # parent를 갱신하기 ★ 이걸 2번 갱신하는 게 맞나...?
    parent[a] = find(a)
    parent[b] = find(b)

    # 3-2. parent가 같으면 -> 순환이므로 break
    if parent[a] == parent[b]:
        rst = i
        break  # for문 탈출

    # 3-2. parent가 다르면 -> 아직 순환이 아니므로 연결하기
    else:
        union(a, b)

print(rst)