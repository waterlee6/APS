# 불량 사용자
'''
제재 아이디 목록의 가능한 경우의 수

banned_id를 돌면서, user_id에서 가능한 경우의 수를 구하기
동일한 user_id가 가능한 경우에는?

user_id가 가능한 조건
1. 길이가 같을 것
2. *이 아닌 경우 알파벳 일치해야 함

DFS로는 어떻게 풀지?
'''
from pprint import pprint
from itertools import product


def solution(user_id, banned_id):
    possible_ids = []  # 모든 경우의 수 리스트를 담을 리스트

    ### banned_id에 있는 id들을 하나하나 user_id와 비교해, 가능한 아이디들을 뽑음
    for searching_id in banned_id:
        # print(f'이번에는 {target_id}를 찾아볼께----------------------')
        cases = []  # searching_id별 가능한 id를 담을 리스트

        for compare_id in user_id:
            # print(f'{compare_id}랑 비교하기')
            possible = True  # while문 탈출 위한 flag

            # 1-1. 길이가 같으면 cases에 넣기
            if len(searching_id) == len(compare_id):
                cases.append(compare_id)
                # print(f'길이가 같아서 추가 : {cases}')

                # 2. 길이가 같은 compare_id에 대해 한 글자씩 비교하기 -> 확실히 다른 글자가 있으면 가능성 없음
                while possible == True:  # 가능성이 있는 동안
                    for i in range(len(compare_id)):  # compare_id와 한 글자 한 글자 비교

                        # 2-1. 한 글자라도 다르면 가능할 수 없으므로 빼기 (*이면 판단 불가)
                        if searching_id[i] != '*' and searching_id[i] != compare_id[i]:
                            cases.pop()  # 방금 넣은 compare_id 빼기
                            possible = False  # flag 표시하고 while문 탈출
                            # print(f'다른 글자가 있어서 제외함')
                            break

                    # 2-2. for문을 다 돌 때까지 중간에 탈출하지 않았다면 가능한 id임 (while문은 탈출해주기)
                    else:
                        possible = False
                        # print('끝까지 살아남음')

            # 1-2. 길이가 다르면 가능성 없으므로 무시
            # else:
            # print('길이가 달라서 추가 안 함')

        # 3. possible_ids에 cases를 추가하기
        possible_ids.append(cases)

    ### possible_ids에 있는 각각의 리스트들로 경우의 수를 구하기
    # if len(banned_id) == len(possible_ids에):
    #     print('맞는 결과')
    # else:
    #     print('틀린 결과')
    '''
    pprint(possible_ids에)
    각 줄에서 하나씩 고름, 이미 선택되었다면 다시 고를 수는 없음,
    2차원 배열에서 한 줄에서 하나씩 고르는 경우의 수 구하기
    [['frodo', 'fradi'],
     ['frodo', 'crodo'],
     ['abc123', 'frodoc'],
     ['abc123', 'frodoc']]
    '''
    # ★★★ 1. product의 인자로 리스트 안에 들어있는 여러 리스트를 넣어서 조합 만들기
    combis = set(product(*possible_ids))
    # print(combis)

    answer = []  # 진짜 최종 정답을 담을 리스트

    # 2. 근데 지금 이 combis의 combi 안에는 같은 값이 두 번 들어있는 경우도 있음
    for combi in combis:
        temp = set(combi)
        if len(banned_id) == len(temp) and temp not in answer:
            answer.append(temp)

    # print(answer)

    return len(answer)