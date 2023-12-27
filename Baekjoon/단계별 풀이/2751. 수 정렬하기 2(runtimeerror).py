# 2751. 수 정렬하기 2
'''
퀵 정렬로 풀어보기
FAQ: https://www.acmicpc.net/board/view/31887
'''

def quick_sort(arr, start, end):  # start = 0, end = len(arr)-1

    # [종료조건] 원소가 하나가 되면 return
    if start >= end:
        return

    # [수행내용]
    pivot = start        # pivot은 첫 번째 원소
    left = start + 1     # left는 pivot의 한 칸 오른쪽
    right = end          # rignt는 가장 마지막 원소

    # 엇갈리면 중단해야 하므로 엇갈리기 전까지만 while문 돌리기 -> 세 번째 if문에서 pivot과 right를 바꾸고 while문 탈출
    while left <= right:
        
        # 1. 한 칸씩 옆으로 이동하기
        # 1-1. 왼쪽에서 탐색 -> pivot보다 큰 값 찾기
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        # 1-2. 오른쪽에서 탐색 -> pivot보다 작은 값 찾기
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        # 2. 교체하기
        # 2-1. 엇갈렸다면 작은 데이터와 pivot을 교체 -> while문 탈출해서 재귀
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]

        # 2-2. 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체 -> 다시 while문 돌기
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # 분할 이후 왼쪽과 오른쪽에서 각각 퀵 정렬 수행
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)


import sys
sys.setrecursionlimit(100000)  # 재귀 최대 깊이를 설정하는 함수
N = int(input())  # N: 수의 개수
arr = []
for _ in range(N):
    arr.append(int(input()))

start = 0
end = len(arr)-1
quick_sort(arr, start, end)
for _ in arr:
    print(_)
