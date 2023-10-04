# 1025. 제곱수 찾기

import sys
sys.stdin = open('input.txt')
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)
'''
[[1, 2, 3],
 [4, 5, 6]]
'''
max_squarenum = 0  # 완전제곱수의 최대값을 저장할 변수

for i in range(N):
    for j in range(M):
        temp = ''  # 각 자리에서의 정수를 저장할 변수(j마다 초기화)


        # 행의 공차 id는 0부터 N-1까지 가능
        for id in range(N):
            # 열의 공차 jd는 0부터 M-1까지 가능
            for jd in range(M):
                
                # 벽 세우기
                if i+id <= N-1 and j+jd <= M-1:
                    temp += str(arr[i+id][j+jd])

                    print(temp)

        # # 만들어진 temp가 완전 제곱수인지 확인
        # if temp == 완전 제곱수:
        #     if temp > max_squarenum:
        #         max_squarenum = temp
        # else:  # 완전 제곱수가 아니면 다음으로
        #     continue