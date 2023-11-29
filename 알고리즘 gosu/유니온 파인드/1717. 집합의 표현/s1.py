# 1717. 집합의 표현

# 1. find 함수 만들기
# 특정 원소의 대표 노드를 찾아가는 함수 (원소 = 대표노드 이면 자기자신이 대표노드)
def find(a):
    # [종료조건] 대표 노드가 자기 자신이면 return
    if parent[a] == a:
        return parent[a]
    # [수행내용]
    parent[a] = find(parent[a])  # ★★★ 이 값이 return 되었을 때 받아줄 변수가 필요함
    return parent[a]

    # root = find(parent[a])
    # return root


# 2. union 함수 만들기
# 두 원소의 대표 노드가 다를 경우 작은 쪽으로 대표 노드를 변경하는 함수
def union(a, b):
    x = min(a, b)
    y = max(a, b)
    root_a = find(x)
    root_b = find(y)
    # 3-1. 두 노드의 대표 노드가 같다면 이미 같은 집합에 있는 것이므로 넘어감
    if root_a == root_b:
        return
    # 3-2. 두 노드의 대표 노드가 다르다면 다른 집합에 있는 것이므로 합쳐야 함
    parent[root_b] = root_a
    return


# 3. parent 배열 만들기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)  # 재귀 최대 깊이를 설정하는 함수
n, m = map(int, input().split())
parent = [n for n in range(n+1)]  # [0, 1, 2, 3, 4, 5, 6, 7]

# 4. 주어진 연산 수행하기
for i in range(m):
    op, a, b = map(int, input().split())   # op: operation
    if op == 0:      # op가 0이면 a와 b를 s합집합하기
        union(a, b)
        print(f'{i}번째 parent : {parent}')
    elif op == 1:    # op가 1이면 a와 b가 같은 집합에 포함되었는지 확인해서 답을 출력하기
        a_root = find(a)
        b_root = find(b)
        if a_root == b_root:
            print(f'{i}번째 parent : {parent}')
            print(f'{i}번째 YES')
            # print('YES')
        else:
            print(f'{i}번째 parent : {parent}')
            print(f'{i}번째 NO')
            # print('NO')
