# 1806. 부분합
'''
연속된 수들의 부분합 중에서 합이 s 이상이 되는 것 중 가장 짧은 것의 길이 구하기
조건을 만족하는 해가 없을 경우 0을 출력

같은 방향으로 진행하는 투 포인터 활용

s 이상이 되는 것 중 가장 짧은 것이므로, s 이상이 되는 순간 바로 start를 한 칸 이동시킴

합이 s 이상이다 -> start를 한 칸 전진
합이 s 미만이다 -> end를 한 칸 전진
start와 end가 한 칸에서 만났을 때 합이 s 이상이면? -> ???

arr의 마지막에서 정답이 나오는 경우가 계속 에러 발생함
'''
import sys
input = sys.stdin.readline

n, s = map(int, input().split())  # n: 수열의 길이, s: 부분합 목표
arr = list(map(int, input().split()))

# 투 포인터 알고리즘 구현
start = 0
end = 0
temp_sum = arr[start]
min_length = 100000  # 가장 짧은 연속된 수의 길이를 담을 변수

while True:
    # 1. s보다 크거나 같다면 start를 한 칸 이동
    if temp_sum >= s:
        length = end - start + 1
        if min_length > length:
            min_length = length
        temp_sum -= arr[start]   # start를 앞으로 한 칸 이동시키므로 빼기
        start += 1

    # 2. s보다 작으면 end를 한 칸 이동
    else:
        end += 1
        if end == n:  # while문을 최종적으로 탈출하는 위치
            break
        temp_sum += arr[end]

if min_length == 100000:
    print(0)
else:
    print(min_length)
