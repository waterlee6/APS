# 4195. 친구 네트워크

'''
새로운 노드가 주어졌을 때,
기존에 있는 노드와 연결이 되는지 안되는지 확인
전체 합집합에 몇 개의 노드가 연결되어 있는지 확인
처음에 list로 만들었다가 dict로 변경

string 타입도 <, > 연산이 가능한 것이 포인트!!
그럼 indexing을 따로 만들 필요가 없지, 그냥 parent로 대소비교 하면 되니까
'''

# find 함수
def find(a):
    # [종료조건]
    if parent[a] == a:
        return parent[a]
    # [수행내용]
    parent[a] = find(parent[a])
    return parent[a]


# union 함수
def union(a, b):
    a_root = find(a)
    b_root = find(b)

    if a_root < b_root:    # a_root 쪽으로 합치기
        parent[b_root] = a_root  # parent 경로 기록
        friends[a_root] = friends[b_root] = friends[a_root] + friends[b_root]  # root node끼리 비교해서 친구 수를 합치기

    elif a_root > b_root:  # b_root 쪽으로 합치기
        parent[a_root] = b_root  # parent 경로 기록
        friends[a_root] = friends[b_root] = friends[a_root] + friends[b_root]  # root node끼리 비교해서 친구 수를 합치기


import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    F = int(input())  # F: 친구 관계의 수
    parent = {}       # 유니온 파인드 구현을 위한 parent
    friends = {}      # 네트워크의 친구 수를 기록하기 위한 dictionary

    for i in range(F):
        f1, f2 = input().split()

        # 1. f1과 f2를 parent에 기록하기
        for one in [f1, f2]:
            if one not in parent.keys():
                parent[one] = one # 기존에 없으면 -> 자기자신으로 새로 기록
                friends[one] = 1  # 친구 관계를 셀 dict에도 key값 저장


        # print(f'[{f1}, {f2}]')
        # print(f'{i}번째 union 전 parent {parent}')
        # print(f'{i}번째 union 전 friends {friends}')

        # 2. f1과 f2를 union 하기
        union(f1, f2)
        # print(f'{i}번째 union 후 parent {parent}')
        # print(f'{i}번째 union 후 friends {friends}')
        # print()

        # 정답 출력
        ans = friends[find(f1)]
        print(ans)

