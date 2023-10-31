# 17472. 다리 만들기 2

'''
0은 바다, 1은 땅
모든 섬을 연결하는 다리 길이의 최솟값을 출력, 불가능할 시 -1
'''

from pprint import pprint

N, M = map(int, input().split())  # N: 지도의 세로 크기, M: 지도의 가로 크기
arr = [list(map(int, input().split())) for _ in range(N)]


