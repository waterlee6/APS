# 7576. 토마토
# 며칠이 지나면 토마토가 다 익는지 최소 일수 구하기
# 1: 익은 토마토 / 0: 익지 않은 토마토 / -1: 토마토가 들어있지 않음

import sys
sys.stdin = open('input.txt')
M, N = map(int, input().split())  # M: 열의 개수, N: 행의 개수
arr = [list(map(int, input().split())) for _ in range(N)]

'''
1을 찾기
1이 하나도 없으면 -> -1
1과 연결되어 있는 0이 있는지 찾기 (거리는 1)

'''

for