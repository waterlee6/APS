# 보석 쇼핑
'''
모든 보석을 하나 이상 포함하는 가장 짧은 구간을 return
가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return
가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return
'''

import copy

def solution(gems):
    types = list(set(gems))  # 보석의 종류 파악하기 위해 중복 제거
    n = len(types)  # n의 최솟값은 types(최소한 types개는 있어야 하므로), 최대값은 len(gems)
    start = 0
    end = 0
    escape = False

    while n <= len(gems) and escape == False:

        for i in range(len(gems) - n + 1):
            checks = []  # 모든 종류를 포함하는지 확인 위한 리스트

            for j in range(n):
                if gems[i + j] not in checks:
                    checks.append(gems[i + j])

            # n만큼 다 돌았을 때 checks의 길이가 types와 같으면 모든 종류를 포함하는 것이므로
            if len(checks) == len(types):
                start = i + 1
                end = i + n
                escape = True
                break

        # gems를 한 바퀴 돌 때까지 target을 발견하지 못할 경우 n을 1 증가시키기
        n += 1

    answer = [start, end]
    return answer