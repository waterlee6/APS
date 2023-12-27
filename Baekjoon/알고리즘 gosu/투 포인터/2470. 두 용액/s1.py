# 2470. 두 용액
'''
arr의 서로 다른 두 수의 합의 절댓값이 0에 가장 가까운 경우 찾기
조건을 만족하는 답이 두 개 이상인 경우에는 아무거나 하나 출력하므로 먼저 나온 정답을 출력하기

산성 용액/알칼리 용액이 혼합되어 있으면 무조건 두 개를 섞어야 특성값이 0에 가까워지나? => NO
-99 -98 -97 1 2 56 57

두 수를 골라서 더한다 -> 더한 값의 절댓값을 본다 -> 절댓값이 가장 작은 경우가 정답
근데 이걸 투 포인터로 어떻게 찾지?

>> 투 포인터 알고리즘 <<
start, end 모두 0 → n-1 방향으로 이동하는 게 아니라
start는 0 → n-1로, end는 n-1 → 0 방향으로 이동하는 투 포인터를 구현
* 두 수의 합이 음수이면 작은 수를 늘리고
* 두 수의 합이 양수이면 큰 수를 줄이기
'''
import sys
input = sys.stdin.readline

n = int(input())       # n: 전체 용액의 수
arr = list(map(int, input().split()))
arr.sort()             # 투 포인터 알고리즘 적용 위해 오름차순 정렬하기


# 투 포인터 알고리즘 구현
temp_sum = 2000000000  # 두 수의 합의 절댓값을 담을 변수
ans1 = 0
ans2 = 0
start = 0
end = n-1

while start < end:
    # 1. 두 수를 더한 값이 0이면 바로 break
    if arr[start] + arr[end] == 0:
        ans1, ans2 = arr[start], arr[end]
        # print('0이 되었음!')
        # print(ans1, ans2)
        break

    # 2. 두 수를 더한 값의 절댓값이 기존보다 작으면 교체
    if abs(temp_sum) > abs(arr[start] + arr[end]):
        temp_sum = arr[start] + arr[end]   # ★★★ 여기서 temp_sum을 abs(arr[start] + arr[end])로 업데이트 하지 말 것
        ans1, ans2 = arr[start], arr[end]  # temp_sum일 때의 두 용액의 특성값이 ans1, ans2가 됨

    # 3. start와 end를 이동시키기
    # 여기서 temp_sum 값과 비교해서 계속 오답 처리... temp_sum과 비교하는 게 아니라 현재 start, end 위치에서의 값과 비교해야 함
    # 3-1. 현재 자리에서의 합이 양수이면 end를 한 칸씩 줄이기
    if arr[start] + arr[end] > 0:          # ★★★ temp_sum의 값과 비교하지 말 것
        end -= 1
    # 3-2. 현재 자리에서의 합이 음수이면 start를 한 칸씩 늘리기
    elif arr[start] + arr[end] < 0:        # ★★★ temp_sum의 값과 비교하지 말 것
        start += 1

# print('while문 탈출함')
# print(ans1, ans2)

ans = [ans1, ans2]
ans.sort()
print(*ans)