# 4195. 친구 네트워크

'''
새로운 노드가 주어졌을 때,
기존에 있는 노드와 연결이 되는지 안되는지 확인
전체 합집합에 몇 개의 노드가 연결되어 있는지 확인
처음에 list로 만들었다가 dict로 변경
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

    if a_root < b_root:
        parent[b_root] = a_root
    elif a_root > b_root:
        parent[b_root] = a_root


T = int(input())
for tc in range(T):
    F = int(input())  # F: 친구 관계의 수
    parent = {}     # 유니온 파인드 구현을 위한 parent { name : check }
    friends = {}    # key별로 몇 명의 친구가 있는지 누적하기 위한 dict
    # check = 0       # parent의 인덱스를 기록하기 위한 변수
    for i in range(F):
        f1, f2 = input().split()

        # f1과 f2를 parent에 기록하기
        for one in [f1, f2]:
            # 기존에 없으면 -> 자기자신으로 새로 기록
            if one not in parent.keys():
                parent[one] = one
                # friends[one] = 1  # 친구 관계를 셀 dict에도 key값 저장
            # 이미 있으면 -> pass


        print(f'{i}번째 union 전 parent {parent}')
        # print(f'{i}번째 union 전 friends {friends}')

        # f1과 f2를 union 하기
        # union(parent[f1], parent[f2])
        # print(f'{i}번째 union 후 parent {parent}')

        # 각 시점의 root node에 친구 관계의 수를 기록 -> root node는
        #
        # print(f'{i}번째 union 후 friends {friends}')
        print()


        


