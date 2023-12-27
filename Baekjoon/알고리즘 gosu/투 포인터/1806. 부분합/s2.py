# 1806. 부분합
'''
나동빈 유튜브 코드 그대로 썼는데 오답 나오네
'''
import sys
input = sys.stdin.readline

n, s = map(int, input().split())  # n: 수열의 길이, s: 부분합 목표
arr = list(map(int, input().split()))

# 투 포인터 알고리즘 구현
temp_sum = 0
end = 0
min_length = 100000  # 가장 짧은 연속된 수의 길이를 담을 변수

for start in range(n):

    # end를 가능한 만큼 이동시키기
    while temp_sum < s and end < n:
        temp_sum += arr[end]
        end += 1

    if temp_sum >= s:
        length = end - start + 1
        if min_length > length:
            min_length = length

    temp_sum -= arr[start]

if min_length == 100000:
    print(0)
else:
    print(min_length)
