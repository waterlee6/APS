# 9205. 맥주 마시면서 걸어가기
'''
[문제 이해]
맥주 한 박스는 20개 들이 
50미터를 가기 전에 맥주 한 병을 마셔야 함
처음에 가지고 있는 20병으로 갈 수 있는 최대 거리는 1000미터(20*50)
편의점에서 빈 병은 버리고 새 맥주를 살 수 있음 

[풀이방법]
home에서 end까지 거리가 1000 이하라면 바로 갈 수 있음
만약 1000 초과라면 중간에 편의점을 들려야 함 
편의점에서는 항상 맥주를 20병 다 채운다고 가정
중간 편의점에서 end까지 거리가 1000 이하라면 바로 갈 수 있음

1. 지금 자리에서 갈 수 있는 편의점의 위치를 BFS로 다 탐색
2. 각각의 편의점에서 갈 수 있는 편의점을 다시 탐색
3. 탐색 과정 중 end에 도달하는 경우가 있다면 'happy'로 하고 break
4. 모든 노드를 탐색했는데도 end에 가지 못했다면 'sad'
5. 직선 거리가 아닌 좌표로 주어졌기 때문에 거리를 계산하기 위한 함수가 하나 더 필요함 
'''
from collections import deque
import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')


# 두 좌표 간의 거리를 재는 함수 
def distance(A, B):
    rst = abs(A[0]-B[0]) + abs(A[1]-B[1])
    return rst


TC = int(input())
for _ in range(TC):
    n = int(input())  # n : 편의점의 개수
    home = tuple(map(int, input().split()))  # 상근이의 집 좌표 
    stores = []                               # 편의점 좌표 
    for _ in range(n):
        stores.append(tuple(map(int, input().split())))
    end = tuple(map(int, input().split()))   # 페스티벌 좌표 

    q = deque()
    q.append(home)
    visited = [False] * n  # 편의점 개수만큼 visited 만들기 
    ans = 'sad'
    
    while q:
        # 디큐하기 
        point = q.popleft()
        if distance(point, end) <= 1000:
            ans = "happy"
            break

        # 인큐하기 
        for i in range(n):
            if distance(point, stores[i]) <= 1000 and visited[i] == False:
                q.append(stores[i])
                visited[i] = True   # 방문표시 

    print(ans)