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

def find(a):
    # [종료조건]
    if parent[a] == a:
        return a
    # [수행내용]
    parent[a] = find(parent[a])
    return parent[a]


import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)
# sys.stdin = open('input.txt')

N = int(input())  # N: 도시의 수
M = int(input())  # M: 여행계획 도시의 수
arr = [[0] * (N+1)]  # 도시번호와 인덱스 맞추기 위해 0행, 0열 추가
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))
route = list(map(int, input().split()))  # route: 여행 계획
check = ''  # 탐색 결과를 표시할 변수
# print(arr)

# 1. 도시 N의 parent 배열을 만들기 -> 처음에는 자기 자신이 parent
parent = [n for n in range(N+1)]  # [0, 1, 2, 3]
# print(f'탐색 전: {parent}')

# 2. arr를 역 행/역 열 탐색하면서 각 행별로 루트 노드를 찾아나가기
for i in range(N, 0, -1):      # i: N -> 1
    for j in range(N, 0, -1):  # j: N -> 1
        if arr[i][j] == 1 and j < parent[i]:
            parent[i] = j
# print(f'탐색 후: {parent}')

# 3. 최종적으로 완성된 parent 배열에서 여행 계획 도시들이 모두 하나의 루트 노드에 속해있는지 확인 -> find 함수
for m in range(M-1):
    if find(route[m]) == find(route[m+1]):
        check = "YES"
    else:
        check = "NO"
        break

print(check)