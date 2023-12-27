# 2174. 로봇 시뮬레이션

import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

A, B = map(int, input().split())  # A: 가로 크기, B: 세로 크기
N, M = map(int, input().split())  # N: 로봇 개수, M: 명령 개수
robot = [[]]  # 로봇의 초기 위치, 로봇 번호와 맞추기 위해 0번 채우고 시작
for _ in range(N):
    robot.append(list(input().split()))
order = []  # 로봇에 내리는 명령
for _ in range(M):
    order.append(list(input().split()))
# print(robot)
# print(order)

# 1. 땅의 좌표를 만들기
arr = [[0] * (A+1) for _ in range(B+1)]   # 좌표와 맞추기 위해 한 칸씩 추가

# 2. 로봇의 위치 찾아서 명령을 순차적으로 실행
# 모든 로봇에게 명령을 내리는 게 아닐 수도 있음
for n in range(1, N+1):  # 일단 모든 로봇의 위치는 파악해야 하므로 robot 리스트에서 순회
                         # 명령의 로봇 번호와 일치시키기 위해 1부터 N까지 순회
    robot[n]  # n번째 로봇의 현재 위치

    for m in range(M):
        if int(order[m][1]) == n:
            # 명령을 수행
    


# 3. 땅의 밖으로 나가는지 확인

# 4. 다른 로봇에 충돌하는지 확인