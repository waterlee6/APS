'''
델타 탐색 사방향이 우하좌상인데
우로 간다 → 좌에서 왔다
하로 간다 → 상에서 왔다
좌로 간다 → 우에서 왔다
상으로 간다 → 하에서 왔다

visited 배열 원소 : i, j, post_dr
hq 배열 원소 : cost, i, j, post_dr
'''

from pprint import pprint
from heapq import heappush, heappop

def solution(board):
    N = len(board)  # 배열의 한 변의 길이
    INF = 10e9      # 무한대

    # 방향 표시를 위한 3차원 visited 생성
    visited = [[[INF] * 4 for _ in range(N)] for _ in range(N)]

    # 델타탐색할 사방향
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # hq 배열 + 시작점 인큐 (시작점은 post_dr 값을 -1로 설정)
    hq = [(0, 0, 0, -1)]  # cost, i, j, post_dr

    # visited에 시작점 표시
    visited[0][0][0] = 0  # i, j, post_dr

    # hq에 다음 탐색할 노드가 남아있는 동안 반복
    while hq:
        cost, i, j, post_dr = heappop(hq)

        # heappop한 값에 대해 델타탐색
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]

            # 벽 세우기
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0:

                # 1. 시작점일때 (직선이동만 가능)
                if post_dr == -1:
                    visited[ni][nj][d] = cost + 100
                    heappush(hq, (cost + 100, ni, nj, d))

                # 2. 시작점이 아닐때
                else:
                    # 2-1. 직선이동일 때
                    if (post_dr + d) % 2 == 0:

                        # 기존 visited의 cost 보다 낮을 때만 방문하기
                        if cost + 100 <= min(visited[ni][nj]):
                            visited[ni][nj][d] = cost + 100
                            heappush(hq, (cost + 100, ni, nj, d))

                    # 2-2. 코너이동일 때
                    elif (post_dr + d) % 2 == 1:

                        # 기존 visited의 cost 보다 낮을 때만 방문하기
                        if cost + 600 <= min(visited[ni][nj]):
                            visited[ni][nj][d] = cost + 600
                            heappush(hq, (cost + 600, ni, nj, d))

    answer = min(visited[N - 1][N - 1])
    # print(answer)
    return answer


board=[
    [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
solution(board)