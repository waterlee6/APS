# 5656. 벽돌 깨기

from pprint import pprint
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())  #N: 구슬을 쏘는 횟수, W: 행렬의 가로 길이, H: 행렬의 세로 길이
    arr = [list(map(int, input().split())) for _ in range(H)]
    # print(N, W, H)  #3 10 10
    # pprint(arr)
    '''
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [1, 0, 3, 0, 1, 1, 0, 0, 0, 1],
     [1, 1, 1, 0, 1, 2, 0, 0, 0, 9],
     [1, 1, 4, 0, 1, 1, 0, 0, 1, 1],
     [1, 1, 4, 1, 1, 1, 2, 1, 1, 1],
     [1, 1, 5, 1, 1, 1, 1, 2, 1, 1],
     [1, 1, 6, 1, 1, 1, 1, 1, 2, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
     [1, 1, 7, 1, 1, 1, 1, 1, 1, 1]]
    '''
