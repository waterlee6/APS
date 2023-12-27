# 1976. 여행 가자

'''
같은 도시를 여러 번 방문하는 것도 가능하므로,
각 도시(노드)가 하나의 루트 노드에만 속해 있다면 모두 방문이 가능함
노드가 하나의 루트 노드에 속해있는지 확인하기 -> 유니온 파인드

1. 도시 N의 parent 배열을 만들기 -> 처음에는 자기 자신이 parent
2. arr를 역 행 탐색하면서 각 행별로 루트 노드를 찾아나가기
   자기보다 같거나 큰 수에 대해서는 확인하지 않아도 됨
3. 최종적으로 완성된 parent 배열에서 여행 계획 도시들이 모두 하나의 루트 노드에 속해있는지 확인
'''

# 1. find 함수 만들기
# 특정 원소의 대표 노드를 찾아가는 함수 (원소 = 대표노드 이면 자기자신이 대표노드)
def find(a):
    # [종료조건] 대표 노드가 자기 자신이면 return
    if parent[a] == a:
        return parent[a]
    # [수행내용]
    parent[a] = find(parent[a])
    return parent[a]



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


import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)
sys.stdin = open('input.txt')

N = int(input())  # N: 도시의 수
M = int(input())  # M: 여행계획 도시의 수
arr = [[0] * (N+1)]  # 도시번호와 인덱스 맞추기 위해 0행, 0열 추가
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))
route = list(map(int, input().split()))  # route: 여행 계획
check = ''  # 탐색 결과를 표시할 변수
'''
print(arr)
[[0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0],
 [0, 1, 0, 0, 0, 1],
 [0, 0, 0, 0, 1, 0],
 [0, 0, 0, 1, 0, 1],
 [0, 0, 1, 0, 1, 0]]
 '''

# 1. 도시 N의 parent 배열을 만들기 -> 처음에는 자기 자신이 parent
parent = [n for n in range(N+1)]  # 탐색 전: [0, 1, 2, 3, 4, 5]
print(f'탐색 전: {parent}')

# 2. 합칠 수 있는 건 여기서 다 합쳐놓고 시작 -> union


# 3. route를 돌면서 앞에서부터 원소를 두 개씩 비교 -> root node가 다른 원소가 있다면 바로 break
for i in range(M-1):
    if find(i) != find(i+1):  # i와 i+1의 root node가 다르다면 연결되지 않은 것이므로
        check = 'NO'          # check를 NO로 바꾸고
        break                 # 바로 break
