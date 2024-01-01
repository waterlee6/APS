# 네트워크
'''
BFS로 연결되어 있는 그래프의 개수 세기
'''

from collections import deque

def solution(n, computers):
    q = deque()  # BFS 탐색을 위한 q 선언
    visited = [0] * (n)  # 탐색한 컴퓨터를 표시할 배열
    cnt = 0  # 네트워크 개수를 셀 변수

    # visited의 모든 값이 1이 될 때까지 (=모든 컴퓨터를 탐색) 반복
    while True:

        # 1. 종료조건
        if sum(visited) == n:
            break

        # 2. 시작점 구하기
        i = visited.index(0)  # visited에서 아직 방문하지 않은 값 중 가장 작은 값
        q.append(i)
        visited[i] = 1
        cnt += 1  # 새로운 시작점 = 새로운 네트워크

        # 3. BFS 탐색
        while q:
            # 3-1. 디큐하기
            i = q.popleft()

            # 3-2. 인큐하기
            for j in range(n):
                if computers[i][j] == 1 and visited[j] == 0:
                    q.append(j)
                    visited[j] = 1

    answer = cnt
    return answer