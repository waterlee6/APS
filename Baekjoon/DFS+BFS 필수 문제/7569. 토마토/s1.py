# 7569. 토마토
'''
며칠이 지나야 모든 토마토가 익는지
처음부터 모든 토마토가 익어있으면 0, 모두 익지 못하는 상황이면 -1 출력

상자의 가로, 세로에 높이까지 주어져서 3차원 같은 느낌?
3차원 배열의 상, 하 인덱스 설정 방법 -> x좌표, y좌표와 더불어 z좌표를 설정!

익은 토마토에 인접한 토마토를 바로 익혀버리면 그 토마토와 인접한 토마토도 익는 문제 발생
-> q에 익은 토마토의 "좌표"를 일단 넣고, 그 q를 돌며 익히기

토마토가 다 익은 경우, 처음부터 다 익어있던 경우, 다 익을 수 없는 경우를 구분해서 답을 출력해야 함
-> BFS이므로 visited 배열 활용하기
-> visited 따로 쓰지 말고 원래 boxes 배열에다 바로 작성하기 (∵1일차에 익어있으면 1)
'''

from pprint import pprint
from collections import deque
import sys

# 1. 인풋받기
m, n, h = map(int, input().split())  # n: 세로 칸 수, m: 가로 칸 수, h: 높이
boxes = []  # 높이 1의 박스 h개를 담을 리스트

for box in range(h):
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    boxes.append(arr)  # boxes 리스트에 각 층별 box 정보를 append
# pprint(boxes)


# 2. 변수 설정
q = deque()
# visited = [[[False] * m for _ in range(n)] for _ in range(h)]  # visited에는 익은 토마토를 저장?

dx = [0, 1, 0, -1, 0, 0]  # 우하좌상+위/아래
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


no_more_ripen = False  # 더 이상 익은 토마토가 없음을 표시할 변수

# 전체를 탐색해 익은 토마토를 찾아내 q에 넣는 함수
def find_ripen(q, no_more_ripen):
    for z in range(h):  # 각 층별로 확인
        for x in range(n):
            for y in range(m):

                # 방문하지 않은 익은 토마토가 있으면 그 좌표를 q에 저장
                if boxes[z][x][y] == 1:
                    boxes[z][x][y] += 1    # 방문표시
                    q.append((z, x, y))
                    # print('append 함')

    print(f'탐색 1회 마침 : {q}')
    
    # 방문하지 않은 익은 토마토가 없으면 종료
    if len(q) == 0:
        no_more_ripen = True
        print('탐색 종료')



# 찾아낸 익은 토마토의 우하좌상위아래를 탐색해서 안익은 토마토를 익히는 함수
def make_ripen(q, no_more_ripen):

    # q가 있으면 익은 토마토가 있음
    while q:
        z, x, y = q.popleft()
        # print(z, x, y)
        # print(f'pop 함 {q}')
        for d in range(6):  # 총 6방향이므로
             nz, nx, ny = z+dz[d], x+dx[d], y+dy[d]
             if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m: # 벽 세우기
                 if boxes[nz][nx][ny] == 0:
                    boxes[nz][nx][ny] = boxes[z][x][y] + 1
                    print(f'{z, x, y}의 안 익은 토마토 익힘')

    # pprint(boxes)
    # print('----------------------')


# 3. 탐색 수행
cnt = 0
no_more_ripen = True  # 더 이상 익힐 토마토가 없음을 판단하는 변수

while no_more_ripen == False:
    cnt += 1
    find_ripen(q, no_more_ripen)
    make_ripen(q)
    # print(boxes)
    # print('-----------------')
    print(cnt)


# 4. 탐색 종료 후 정답 출력하기
'''
탐색 종료일 때 boxes에 0이 남아 있으면 -1
탐색 종료일 때 0이 없으면 횟수 출력
처음부터 다 익어 있으면 0 출력 
'''
