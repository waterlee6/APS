# 4949. 균형잡힌 세상
'''
괄호가 하나도 없는 경우도 균형잡힌 문자열로 간주됨
그 사이에 있는 문자열도 균형이 잡혀야 한다 -> ?
'''

import sys
input = sys.stdin.readline

while True:
    sen = input()
    # print(len(sen))

    # 종료조건 ★★★
    if len(sen) == 2:
        break

    q = [0]
    for s in sen:
        if s in ['(', '[']:
            q.append(s)

        elif s == ')':
            if q[-1] == '(':
                q.pop()
            else:
                q.append(s)

        elif s == ']':
            if q[-1] == '[':
                q.pop()
            else:
                q.append(s)

    # print(q)
    if len(q) == 1:
        print('yes')
    else:
        print('no')