# 1018. 체스판 다시 칠하기

'''
처음에는 델타탐색으로 상하좌우 탐색을 시도 -> 어차피 자리가 고정되어 있으므로 불필요
(0, 0) 칸에 칠해진 색이 A라고 하면,
짝수 행 -> 짝수 번째
홀수 행 -> 홀수 번째  에 A가 칠해져야 함 (k+l이 짝수)
짝수 행 -> 홀수 번째
홀수 행 -> 짝수 번째  에 A'가 칠해져야 함 (k+l이 홀수)
'''

# import sys
# sys.stdin = open('input.txt')
N, M = map(int, input().split())  # N: 행의 개수, M: 열의 개수
arr = [input() for _ in range(N)]
min_paint = 2500  # 최소로 칠하는 횟수를 저장할 변수

# 1. 제시된 전체 체스판을 순회하기 위한 i, j
for i in range(N-7):  # 8칸의 순회를 돌아야 하므로 범위는 N-7로 제한
    for j in range(M-7):  # 8칸의 순회를 돌아야 하므로 범위는 N-7로 제한
        paint = 0

        # 2. 각 (i, j) 칸으로부터 8*8 보드를 순회하기 위한 k, l
        for k in range(8):
            for l in range(8):

                # 8*8 보드에서 (0, 0)칸의 색에 따라 모든 칸의 색이 정해짐
                # 3. (0, 0)칸이 원래 B인 경우
                if arr[i][j] == 'B':
                    # 3-1. B를 바꾸지 않고 그대로 진행
                    if (k+l) % 2 == 0:            # B가 칠해져야 하는 칸들에서
                        if arr[i+k][j+l] == "W":  # W가 칠해져 있다면
                            paint += 1            # paint에 +1
                    if (k+l) % 2 == 1:            # W가 칠해져야 하는 칸들에서
                        if arr[i+k][j+l] == 'B':  # B가 칠해져 있다면
                            paint += 1            # paint에 +1


                # 4. (0, 0)칸이 원래 W인 경우
                elif arr[i][j] == 'W':
                    # 4-1. W를 그대로 바꾸지 않고 진행
                    if (k+l) % 2 == 0:            # B가 칠해져야 하는 칸들에서
                        if arr[i+k][j+l] == "B":  # W가 칠해져 있다면
                            paint += 1            # paint에 +1
                    if (k+l) % 2 == 1:            # W가 칠해져야 하는 칸들에서
                        if arr[i+k][j+l] == 'W':  # B가 칠해져 있다면
                            paint += 1            # paint에 +1


        # 5. 8*8 보드를 순회하고 나서 min_paint와 비교
        if paint < min_paint:
            min_paint = paint

print(min_paint)