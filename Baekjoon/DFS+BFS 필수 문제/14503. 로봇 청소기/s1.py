# 14503. 로봇 청소기
'''
[문제 이해하기]
로봇 청소기가 청소하는 칸의 개수를 출력 
d : 0 북쪽 / 1 동쪽 / 2 남쪽 / 3 서쪽 
방의 테두리는 무조건 벽이 있음 
'''
from collections import deque
import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

N, M = tuple(map(int, input().split()))
r, c, d = tuple(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# print(N, M)
# print(r, c, d)
# print(arr)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

visited = [[0] * M for _ in range(N)]
cleaned = 0  # 청소된 칸의 개수를 셀 변수 
q = deque()

for i in range(1, N-1):
    for j in range(1, M-1):
        if arr[i][j] == 0 and visited[i][j] == 0:
            cleaned += 1
            visited[i][j] = 1

        for direction in range(4):  # 우하좌상 4방향 
            d
