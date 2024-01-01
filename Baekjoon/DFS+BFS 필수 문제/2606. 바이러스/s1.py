# 2606. 바이러스
'''
1번 정점과 연결되어 있는 정점의 개수 파악 -> BFS로 연결된 모든 노드를 구하기
1번 컴퓨터로 인해 감염되는 컴퓨터의 수 이므로 1번은 제외해야 함
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())  # n: 컴퓨터의 수
m = int(input())  # m: 간선의 개수
arr = [[] for _ in range(n+1)]  # 컴퓨터 번호와 맞추기 위해 앞에 하나 추가

# 인접 리스트 만들기
for _ in range(m):
    i, j = map(int, input().split())
    arr[i].append(j)
    arr[j].append(i)

# BFS 수행하기
q = deque()
visited = [False] * (n+1)
links = []         # 연결된 컴퓨터를 담을 리스트
q.append(1)        # 시작점 인큐
visited[1] = True  # 시작점 visited

while q:
    # 디큐하기
    i = q.popleft()

    # 인큐하기
    for j in arr[i]:
        if visited[j] == False:
            q.append(j)
            visited[j] = True
            links.append(j)

print(len(links))