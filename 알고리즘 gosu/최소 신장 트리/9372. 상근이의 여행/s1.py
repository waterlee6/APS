# 9372. 상근이의 여행

'''
가장 적은 개수의 비행기를 타고 모든 노드를 방문
-> 모든 노드를 연결하는 최소한의 간선 개수는 N-1
이렇게 푸는게 맞나..?
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 국가의 수, M: 비행기의 수
    arr = []  # 비행기 경로
    for _ in range(M):
        arr.append(list(map(int, input().split())))

    ans = N -1
    print(ans)