# 3273. 두 수의 합
'''
이중 for문을 활용하는 완전탐색으로 풀면 시간초과 발생

근데 투 포인터로 어떻게 풀 수 있지?
투 포인터는 start와 end 사이의 모든 값을 더하는 거니까 'start를 이동 -> 감소, end를 이동 -> 증가'라는
공식이 성립하는 거지만, 이 문제는 개별적인 두 값의 합을 구하는 문제인데??

주어진 arr를 오름차순 정렬한 뒤에 투 포인터를 적용하면 위의 규칙을 적용할 수 있음!
투 포인터 알고리즘의 핵심은 start, end 두 인덱스가 한 방향으로만 움직이는 것
'''
import sys
input = sys.stdin.readline

n = int(input())  # n: 수열의 크기
arr = list(map(int, input().split()))
x = int(input())  # x: 찾는 값
temp_sum = 0      # 임시 합
cnt = 0           # 만족하는 쌍의 수를 셀 변수

# 완전탐색으로 풀어보기 -> 시간초과
# for start in range(n-1):
#     for end in range(start+1, n):
#         if arr[start] + arr[end] == x:
#             cnt += 1

# 완전탐색으로 풀어보기(가지치기) -> 시간초과
# for start in range(n-1):
#     if arr[start] >= x:
#         continue
#
#     for end in range(start+1, n):
#         if arr[end] >= x:
#             continue
#         if arr[start] + arr[end] == x:
#             cnt += 1

# 투 포인터로 풀어보기
# 근데 이거랑 이중 for문이랑 왜 시간 차이가 나는지는 모르겠음...
arr.sort()  # 투 포인터 적용 위해 오름차순 정렬 (오른쪽으로 이동할수록 증가하는 것 보장 위해)
for start in range(n-1):  # start < end 이므로 start는 n-1까지 갈 수 없음
    temp_sum = 0          # temp_sum 초기화
    end = start + 1       # send는 항상 start보다 커야 하므로 (start가 바뀌면 end 시작점도 바뀜)
    while temp_sum < x and end < n:
        temp_sum = arr[start] + arr[end]
        end += 1
        if temp_sum == x:
            cnt += 1

print(cnt)