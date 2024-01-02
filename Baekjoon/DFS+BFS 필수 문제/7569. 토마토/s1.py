# 7569. 토마토
'''
며칠이 지나야 모든 토마토가 익는지
상자의 가로, 세로에 높이까지 주어져서 3차원 같은 느낌?
'''
from pprint import pprint

m, n, h = map(int, input().split())  # n: 세로 칸 수, m: 가로 칸 수, h: 높이
boxes = []  # 높이 1의 박스 h개를 담을 리스트
date = 0    # 며칠이 지났는지 셀 변수

for box in range(h):
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    boxes.append(arr)  # boxes 리스트에 각 층별 box 정보를 append

di = [0, 1, 0, -1]  # 우하좌상
dj = [1, 0, -1, 0]

# h == 1일때만 따로 빼기?
# h == 2일때

for k in range(h):  # 각 층별로 확인
    for i in range(n):
        for j in range(m):
            if boxes[k][i][j] == 1:    # 익은 토마토가 있으면

                # 같은 층 익히기
                for d in range(4):   # 우하좌상 4방향을 탐색해서
                    ni, nj = i+di[d], j+dj[d]
                    if 0 <= ni < n and 0 <= nj < m:
                        if boxes[k][ni][nj] == 0:   # 안익은 토마토이면
                            boxes[k][ni][nj] = 1    # 익히기

print(boxes)
                # # 다른 층 익히기
                # if k == 0:      # 위층만 확인
                #     if arr[1][i][j] == 0:
                #         arr[1][i][j] = 1
                #
                # elif k == h-1:  # 아랫층만 확인
                #     if arr[h-2][i][j] == 0:
                #         arr[h - 2][i][j] = 1
                #
                # else:           # 위아래층 확인
                #     if arr[][]
