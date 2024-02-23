# 2573. 빙산
'''
일년마다 동서남북 네 방향으로 붙어있는 0 칸 개수만큼 높이가 감소
빙산이 두 덩어리 이상으로 분리되는 최초의 시간
전부 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0을 출력

1. 1년이 지날 때마다 빙하를 녹이기 -> 델타탐색
2. 몇 개의 덩어리로 분리되었는지 확인하기 -> BFS 
'''
from pprint import pprint
from collections import deque
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
year = 0     # 연도를 셀 변수 

# 델타탐색 방향
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


# [빙하 주변의 바다를 찾는 함수]
def finding(arr, surroundedby):
    for i in range(N):
        for j in range(M):
            for d in range(4):
                ni, nj = i+di[d], j+dj[d]

                # 벽 세우기
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] <= 0 and arr[i][j] > 0:
                    surroundedby[i][j] += 1


# [빙하를 녹이는 함수]
# 더 이상 녹일 빙하가 없을 때를 구분하는 flag를 return 하도록 작성 
def melting(arr, surroundedby):
    no_more_melting = True  # 더 이상 녹일 빙하가 없는지 확인 위한 변수(매번 True로 초기화)
    for i in range (N):
        for j in range(M):
            if surroundedby[i][j] != 0 and arr[i][j] > 0:
                no_more_melting = False   # 하나라도 녹이면 녹일 빙하가 있는 것 
                arr[i][j] -= surroundedby[i][j]
    return no_more_melting


# [몇 개의 덩어리인지 확인해서 정답을 출력하는 함수]
def counting():
    global arr, year
    enough_iceburg = False  # 빙하의 개수가 2개 이상임 확인 위한 변수 
    
    # iceburg가 2개 이상이면 while문 종료
    while enough_iceburg == False:
        year += 1 
        iceburg = 0               # 빙산의 개수 초기화 
        enough_iceburg = False    # 빙산이 2개 이상인지 확인할 flag

        # visited, q, surroundedby 배열은 매번 초기화
        visited = [[0] * M for _ in range(N)]
        q = deque()
        surroundedby = [[0] * M for _ in range(N)]  # 주위 바다의 개수를 표시할 배열

        # finding 함수 실행
        finding(arr, surroundedby)

        # melting 함수 실행, return 값을 변수에 저장
        no_more_melting = melting(arr, surroundedby)
     

        # 빙하가 2개 이상이 되지 않았지만 더 이상 녹일 빙하가 없으면 탈출
        if no_more_melting == True:
            break  # while문 탈출 
        
        # 몇 개의 덩어리인지 확인하는 부분
        while enough_iceburg == False:
            # 1. 아직 방문하지 않은 빙하 찾아서 q에 넣기
            start_search = False   # 탐색을 시작할 첫번째 빙하를 찾았는지 확인 위한 변수
            for i in range(N):
                for j in range(M):
                    if arr[i][j] > 0 and visited[i][j] == 0:
                        q.append((i, j))
                        visited[i][j] = 1    # 디큐할 때가 아니라 인큐할 때 방문처리 
                        iceburg += 1         # 새로운 지점 찾을 때 iceburg +1
                        if iceburg >= 2:
                            enough_iceburg = True
                        start_search = True  # 탐색을 시작할 첫번째 빙하를 찾으면 j for문 break
                        break
                if start_search == True:
                    break                    # i for문 break
            else:                            # for문을 다 도는 동안 start_search가 False이면 더 이상 탐색할 빙하 없음 
                break                        # while문 break

            # 2. start_search=True일 때 연결된 빙하들을 찾아서 q에 넣고 방문표시 하기
            while q:
                i, j = q.popleft()
                for d in range(4):
                    ni, nj = i+di[d], j+dj[d]
                    if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] > 0:
                        q.append((ni, nj))
                        visited[ni][nj] = 1  # 디큐할 때가 아니라 인큐할 때 방문처리 
    
    return iceburg

iceburg = counting()

if iceburg >= 2:
    print(year)
else:
    print(0)