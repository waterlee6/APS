# 1018. 체스판 다시 칠하기

'''
처음에는 델타탐색으로 상하좌우 탐색을 시도 -> 어차피 자리가 고정되어 있으므로 불필요
(0, 0) 칸에 칠해진 색이 A라고 하면,
짝수 행 -> 짝수 번째
홀수 행 -> 홀수 번째  에 A가 칠해져야 함 (k+l이 짝수)
짝수 행 -> 홀수 번째
홀수 행 -> 짝수 번째  에 A'가 칠해져야 함 (k+l이 홀수)
'''
'''
예제 4번에서 자꾸 32가 출력됨
-> 첫번째 칸은 무조건 주어진 색으로만 두고 풀었는데,
첫번째 칸의 색을 바꾸는 경우도 고려해야 함
'''

import sys
sys.stdin = open('input.txt')
N, M = map(int, input().split())  # N: 행의 개수, M: 열의 개수
arr = [input() for _ in range(N)]
min_paint = 2500  # 최소로 칠하는 횟수를 저장할 변수

# 1. 제시된 전체 체스판을 순회하기 위한 i, j
for i in range(N - 7):  # 8칸의 순회를 돌아야 하므로 범위는 N-7로 제한
    for j in range(M - 7):  # 8칸의 순회를 돌아야 하므로 범위는 N-7로 제한
        paint = 0   # paint1과 paint2 중 더 작은 값을 저장하는 변수
        paint1 = 0  # (0, 0)칸이 B라고 가정했을 때 다시 칠하는 횟수
        paint2 = 0  # (0, 0)칸이 W라고 가정했을 때 다시 칠하는 횟수

        # 2. 각 (i, j) 칸으로부터 8*8 보드를 순회하기 위한 k, l
        for k in range(8):
            for l in range(8):

                # 8*8 보드에서 (0, 0)칸의 색에 따라 모든 칸의 색이 정해짐
                # 여기서 (0, 0)칸을 B, W로 정하지 말고
                # 그냥 (k+l)가 짝수인 경우, 홀수인 경우로 나누어 계산한 뒤
                # 더 작은 값을 출력
            
                
                # 3. k+l이 짝수인 칸 -> (0, 0)칸과 같은 색이 칠해지는 칸
                if (k + l) % 2 == 0:
                    if arr[i + k][j + l] == "W":
                        paint1 += 1   # paint1은 (0, 0)이 B라고 가정하므로 W가 칠해진 칸의 개수를 셈
                    elif arr[i + k][j + l] == 'B':
                        paint2 += 1   # paint2는 (0, 0)이 W라고 가정하므로 B가 칠해진 칸의 개수를 셈

                        
                # 4. k+l이 홀수인 칸 -> (0, 0)칸과 다른 색이 칠해지는 칸
                elif (k + l) % 2 == 1:
                    if arr[i + k][j + l] == 'B':
                        paint1 += 1  # paint1은 (0, 0)이 B라고 가정하므로 홀수칸에 B가 칠해진 칸의 개수를 셈
                    elif arr[i + k][j + l] == 'W':
                        paint2 += 2  # paint2는 (0, 0)이 W라고 가정하므로 홀수칸에 W가 칠해진 칸의 개수를 셈

        # 5. paint1과 paint2 중 더 작은 값만 가지고 감
        paint = min(paint1, paint2)

        # 5. 8*8 보드를 순회하고 나서 min_paint와 비교
        if paint < min_paint:
            min_paint = paint

print(min_paint)