# 2751. 수 정렬하기 2
'''
퀵 정렬로 풀었는데 시간초과
-> 병합정렬로 다시 풀어보기
'''

cnt = 0
def merge_sort(unordered_list):
    global cnt
    cnt += 1

    # [종료조건]
    # 나눌 배열의 길이가 1이면 stop
    if len(unordered_list) <= 1:
        return unordered_list

    # [수행내용]
    # 1. unordered_list를 받아서 왼쪽 배열, 오른쪽 배열로 나누기
    middle = len(unordered_list) // 2
    left = merge_sort(unordered_list[:middle])
    # print(f'{cnt}번째 left: {left}')
    right = merge_sort(unordered_list[middle:])
    # print(f'{cnt}번째 right: {right}')

    # 2. return된 left 배열과 right 배열의 요소를 비교해서 합치기
    i = 0     # left를 순회할 인덱스
    j = 0     # right를 순회할 인덱스
    rst = []  # 결과를 담을 리스트

    # 3. left나 right 둘 중 하나라도 모두 탐색하면 while문 빠져나감
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            rst.append(left[i])
            i += 1
        else:
            rst.append(right[j])
            j += 1

    # while문 빠져 나온 후, left혹은 right에 남은 요소들 arr에 넣어주기
    rst += left[i:]
    rst += right[j:]

    return rst


N = int(input())  # N: 수의 개수
arr = []
for _ in range(N):
    arr.append(int(input()))

arr = merge_sort(arr)
for _ in arr:
    print(_)