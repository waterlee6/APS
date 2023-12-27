# 9012. 괄호

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    q = [0]  # 괄호를 하나씩 분해해서 담을 리스트
    ps = input()

    for p in ps:
        # q에 들어있는 마지막 글자가 '('이고 넣을 글자가 ')'이면 VPS
        if q[-1] == '(' and p == ')':
            q.pop()
        else:
            q.append(p)

    if len(q) == 2:
        rst = 'YES'
    else:
        rst = 'NO'

    print(rst)
