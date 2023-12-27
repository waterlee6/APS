# 1956. 운동
# DFS로 사이클 찾는 연습 해보기
'''
(a, b) 쌍이 같은 도로가 여러 개 주어지지 않는다
-> 시작점과 도착점이 같은 두 마을 사이에는 간선이 하나뿐이다.
-> routes[a]에는 단 하나의 원소만 있다는 뜻!!

>> DFS로 사이클 찾기 <<
1. 무향 그래프
  - stack 사용
  - union find
2. 유향 그래프
  - visited 리스트와 fin 리스트를 활용
  - 재귀를 사용해야만 하는 듯?
  - visited 리스트 : 기존의 visited 처럼 노드를 탐색할 때 방문 표시
  - fin 리스트 : 해당 재귀에서 탐색이 종료되었을 때 표시 (해당 노드의 모든 간선을 탐색?)
'''

# DFS로 사이클 찾는 함수(재귀)
# https://bit.ly/3QYPyZc (이중 함수)
# https://bit.ly/3T0cUQI

def dfs(now):  # now: 현재 탐색중인 정점 / visited와 finished를 업데이트하는 함수
    global cnt  # 사이클 여부를 확인하는 변수(기본은 False)

    # 1. visited, stack, path
    visited[now] = True   # i 방문표시

    # 2. dfs 탐색하기
    for new, dis in routes[now]:
        # 2-1. 만약 연결된 정점을 아직 방문하지 않았다면 방문하기 => 재귀 발생
        if visited[new] == False:
            dfs(new)
        # 2-2. 이미 방문한 정점인데 finished 되지 않았다면 => 사이클 발생
        elif finished[new] == False:
            # 2-3. 사이클의 길이 세기
            temp_node = new
            while True:
                cnt += 1
                temp_node = routes[temp_node][0][0]
                if temp_node == new:   # temp_node와 new가 같아지면 한 바퀴를 돈 것이므로
                    break

    # 3. dfs 탐색을 마친 후에 해당 노드를 finished 처리
    finished[now] = True


# DFS로 사이클 찾는 함수(태현오빠)
# def dfs():
#     while True:
#         # 2-1. 현재 위치 i에서 탐색 나갈 j가 있으면
#         for j in range(1, n + 1):
#             if visited[j] == False and routes[i][j] != 0:
#                 path.append(j)
#                 stack.append(j)
#
#                 i = j  # 현태 탐색 중인 노드의 위치 바꾸기
#                 visited[i] = True
#                 break
#
#         # 2-2. 현재 위치 i에서 더 이상 방문할 곳이 없으면 -> 뒷걸음질
#         else:
#             if stack:
#                 i = stack.pop()
#             else:
#                 break


import pprint
from collections import deque
import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

n, m = map(int, input().split())  # n: 마을의 개수, m: 도로의 개수

# 간선 정보를 인접 행렬에 담기
# routes = [[0] * (n+1) for _ in range(n+1)]
# for _ in range(m):
#     a, b, w = map(int, input().split())
#     routes[a][b] = w

# 간선 정보를 인접 리스트에 담기
routes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    routes[a].append((b, w))

# DFS 위한 visited, searched 리스트 만들기
visited = [False] * (n+1)   # 방문한 노드를 표시
finished = [False] * (n+1)  # 탐색 완료한 노드를 표시

# 사이클의 길이를 확인하는 변수 (없을 경우 0)
cnt = 0
print('함수 실행 전-------------')
print(visited)   # [False, False, False, False]
print(finished)  # [False, False, False, False]

# DFS로 사이클 여부를 확인
dfs(1)
print('함수 실행 후-------------')
print(visited)
print(finished)
print(cnt)
