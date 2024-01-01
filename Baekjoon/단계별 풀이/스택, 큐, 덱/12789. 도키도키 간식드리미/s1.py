# 12789. 도키도키 간식드리미

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []

# arr를 돌면서 순서가 맞으면 pass하고 아니면 stack으로 보내기
latest = 0
for i in arr:
    if i == latest + 1:
        latest += 1
        # print(f'{i}이 줄에서 빠져나감 : {stack}')
        # print('latest : ', latest)

        # stack에 원소가 있고, 원소가 들어갈 차례면 계속 빼기
        while stack and stack[-1] == latest + 1:
            stack.pop()
            latest += 1
            # print(f'{latest}이 stack에서 빠져나감 : {stack}11')
            # print('latest : ', latest)
    else:
        stack.append(i)
        # print(f'stack에 {i}추가 : {stack}')
        # print('latest : ', latest)

if latest == N:
    ans = 'Nice'
else:
    ans = 'Sad'

print(ans)