# 2798. 블랙잭

# 재귀를 사용해 조합을 구하는 함수 확실히 기억하기

# N장 중 3장을 고르는 조합
# 각 경우를 완전탐색으로 조사해서 가장 큰 수를 반환


# 조합과 각 경우의 합을 구하는 재귀함수
def combi_sum(n, r):  # n개 중 r개를 고르는 조합, m은 합의 최댓값
    global max_sum
    global m

    # [종료조건]
    if r == 0:   # 고를 자리가 남지 않은 경우 return -> 이 경우에 합을 계산
        temp_sum = sum(temp)
        if temp_sum <= m:
            if temp_sum > max_sum:
                max_sum = temp_sum

    elif n < r:  # 고를 자리보다 숫자가 적게 남은 경우 return
        return

    # [수행내용]
    else:
        temp[r-1] = arr[n-1]
        combi_sum(n-1, r-1)
        combi_sum(n-1, r)


# import sys
# sys.stdin = open('input.txt')
n, m = map(int, input().split())  # n: 카드의 개수, m: 만들어야 하는 값
arr = list(map(int, input().split()))  # arr: 주어진 N장의 카드
r = 3           # r: 고를 카드의 수 (3장)
temp = [0] * r  # 조합을 임시 저장할 변수
max_sum = 0  # 합의 최댓값을 저장할 변수

combi_sum(n, r)
print(max_sum)
