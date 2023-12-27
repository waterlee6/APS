# 28278. 스택 2
'''
2번 명령이 좀 헷갈렸는데 스택이 비어있지 않다면 맨 위의 정수(가장 나중에 추가된 정수)를 빼고 그 정수를 출력하라는 의미
'''
import sys
input = sys.stdin.readline

n = int(input())  # n: 명령의 수
orders = []  # 명령을 저장할 리스트
for _ in range(n):
    order = list(map(int, input().split()))
    orders.append(order)

stack = []
cnt = 0
for order in orders:
    cnt += 1
    if order[0] == 1:
        stack.append(order[1])
        # print(f'(명령 1){cnt}번째 stack: {stack}')

    elif order[0] == 2:
        if stack:
            if stack:
                print(stack.pop())
            else:
                print(-1)
            # print(f'(명령 2){cnt}번째 stack: {stack}')

        else:
            print(-1)
            # print(f'(명령 2){cnt}번째 stack: {stack}')


    elif order[0] == 3:
        print(len(stack))
        # print(f'(명령 3){cnt}번째 stack: {stack}')


    elif order[0] == 4:
        if stack:
            print(0)
            # print(f'(명령 4){cnt}번째 stack: {stack}')

        else:
            print(1)
            # print(f'(명령 4){cnt}번째 stack: {stack}')


    elif order[0] == 5:
        if stack:
            print(stack[-1])
            # print(f'(명령 5){cnt}번째 stack: {stack}')

        else:
            print(-1)
            # print(f'(명령 5){cnt}번째 stack: {stack}')
