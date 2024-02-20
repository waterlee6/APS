# 경주로 건설

'''
경주로 건설을 위한 최소 비용
직선 도로 : 100원 , 코너 : 500원
출발점과 도착점은 항상 0
직선 도로 : 칸 개수 - 1
코너 : ??

코너 생각 안하고 직선 도로만 있다고 했을 때 최단 거리는 어떻게 구하지?

코너를 세는 방법이 어려울 것 같은데

=============================
* 직전에 진행해 온 방향을 알아야 직선인지 코너인지 알 수 있으므로
  한 점의 4개의 진행방향을 저장하기 위해 [우측에서, 아래서, 좌측에서, 위에서]로 visited를 설정
* 각각의 점에 대해 네 방향으로 탐색을 하고, 그 점까지 갈 수 있는 최솟값을 저장
* 힙큐에 다음에 방문할 점을 넣어두고 힙큐가 사라질 때까지 반복
* 힙큐를 사용하는 이유? 비용 순으로 pop 가능 -> 비용이 더 작을 때만 갱신하는데 비용이 큰 경우는 뒤로 밀리기 때문에 더 효율적

'''
from pprint import pprint
from heapq import heappush, heappop


'''
경주로 건설을 위한 최소 비용
직선 도로 : 100원 , 코너 : 500원 
출발점과 도착점은 항상 0
직선 도로 : 칸 개수 - 1
코너 : ??

코너 생각 안하고 직선 도로만 있다고 했을 때 최단 거리는 어떻게 구하지? 

코너를 세는 방법이 어려울 것 같은데

=============================
* 직전에 진행해 온 방향을 알아야 직선인지 코너인지 알 수 있으므로
  한 점의 4개의 진행방향을 저장하기 위해 [우측에서, 아래서, 좌측에서, 위에서]로 visited를 설정 
* 각각의 점에 대해 네 방향으로 탐색을 하고, 그 점까지 갈 수 있는 최솟값을 저장
* 힙큐에 다음에 방문할 점을 넣어두고 힙큐가 사라질 때까지 반복
* 힙큐를 사용하는 이유? 비용 순으로 pop 가능 -> 비용이 더 작을 때만 갱신하는데 비용이 큰 경우는 뒤로 밀리기 때문에 더 효율적 

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
    INF = 10e9

    # 방향 표시를 위한 3차원 visited 생성
    visited = [[[INF] * 4 for _ in range(N)] for _ in range(N)]

    # 직전 진행 방향 인덱스 설정
    # 델타 탐색 사방향이 우하좌상인데
    # 우로 간다 → 좌에서 왔다
    # 하로 간다 → 상에서 왔다
    # 좌로 간다 → 우에서 왔다
    # 상으로 간다 → 하에서 왔다
    # from = {
    #     0 : 'horizontal',
    #     1 : 'vertical',
    #     2 : 'horizontal',
    #     3 : 'vertical',
    # }

    # 델타탐색할 사방향
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # hq 배열 + 시작점 인큐 (시작점은 post_dr 값을 -1로 설정)
    hq = [(0, 0, 0, -1)]  # cost, i, j, post_dr

    # visited에 시작점 표시
    visited[0][0][0] = 0  # i, j, 방향

    # hq에 다음 탐색할 노드가 남아있는 동안 반복
    while hq:
        cost, i, j, post_dr = heappop(hq)
        # print(f'새로운 값 pop: ({cost}, {i}, {j}, {post_dr})')

        # heappop한 값에 대해 델타탐색
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            # print(f'새로운 ni와 nj : {ni}, {nj}')

            # 벽 세우기
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0:

                # 1. 시작점일때 (직선이동만 가능)
                if post_dr == -1:
                    visited[ni][nj][d] = cost + 100
                    heappush(hq, (cost + 100, ni, nj, d))
                    # print(f'시작점일 때 push함 : {(cost+100, ni, nj, d)}')

                # 2. 시작점이 아닐때
                else:
                    # 2-1. 직선이동일 때
                    if (post_dr + d) % 2 == 0:

                        # 기존 visited의 cost 보다 낮을 때만 방문하기
                        if cost + 100 <= min(visited[ni][nj]):
                            visited[ni][nj][d] = cost + 100
                            heappush(hq, (cost + 100, ni, nj, d))
                            # print(f'직선이동일 때 push함, {(cost+100, ni, nj, d)}')

                    # 2-2. 코너이동일 때
                    elif (post_dr + d) % 2 == 1:

                        # 기존 visited의 cost 보다 낮을 때만 방문하기
                        if cost + 600 <= min(visited[ni][nj]):
                            visited[ni][nj][d] = cost + 600
                            heappush(hq, (cost + 600, ni, nj, d))
                            # print(f'코너이동일 때 push함, {(cost+600, ni, nj, d)}')

        # print(hq)
        # print('==========================')
    answer = min(visited[N - 1][N - 1])
    print(answer)
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