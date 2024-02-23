# 9205. 맥주 마시면서 걸어가기

import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')


def distance(A, B):
    rst = abs(A[0]-B[0]) + abs(A[1]-B[1])
    return rst


TC = int(input())
for _ in range(TC):
    n = int(input())  # n : 편의점의 개수
    home = tuple(map(int, input().split()))
    store = []
    for _ in range(n):
        store.append(tuple(map(int, input().split())))
    festival = tuple(map(int, input().split()))

    print(home)
    print(store)
    print(festival)

    