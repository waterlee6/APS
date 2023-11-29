# 1956. 운동
'''
개선된 다익스트라 알고리즘, 플로이드 워셜, DFS로 푼 사람 등 다양한 정답이 있는 듯...
플로이드 워셜은 pypy로만 통과가 되고, 다익스트라로 풀어야 python에서도 통과가 되는 듯
https://velog.io/@nkrang/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1956-%EC%9A%B4%EB%8F%99-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC

※ 두 마을을 왕복하는 경우도 사이클에 포함됨에 주의
'''

# DFS로 사이클 찾는 함수
def dfs(i):  # i: 현재 탐색중인 정저
    # 1. visited, stack, path
    visited = [False] * (n+1)
    visited[i] = True   # i 방문표시
    path = [i]          # 탐색 경로를 저장할 리스트, i를 저장하고 시작
    stack = []

    # 2. dfs 탐색하기
    while True:
        # 2-1. 현재 위치 i에서 탐색 나갈 j가 있으면
        for j in range(1, n+1):
            if visited[j] == False and routes[i][j] != 0:
                path.append(j)
                stack.append(j)

                i = j  # 현태 탐색 중인 노드의 위치 바꾸기
                visited[i] = True
                break

        # 2-2. 현재 위치 i에서 더 이상 방문할 곳이 없으면 -> 뒷걸음질
        else:
            if stack:
                i = stack.pop()
            else:
                break




import pprint
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n: 마을의 개수, m: 도로의 개수
routes = [[0] * (n+1) for _ in range(n+1)]

# 간선 정보를 인접 행렬에 담기
for _ in range(m):
    a, b, w = map(int, input().split())
    routes[a][b] = w

# DFS로 사이클 여부를 확인
