# 4195. 친구 네트워크

'''
새로운 노드가 주어졌을 때,
기존에 있는 노드와 연결이 되는지 안되는지 확인
전체 합집합에 몇 개의 노드가 연결되어 있는지 확인
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
    parent = []  # 유니온 파인드 구현을 위한 parent
    indexing = []   # parent의 인덱스 설정을 위한 딕셔너리 -> 이 넣은 순서를 parent의 인덱스로 사용
    for _ in range(F):
        f1, f2 = input().split()
        print(f'f1 : {f1}, f2 : {f2}')
        for one in [f1, f2]:
            if one not in indexing:
                indexing.append(one)
                initial = indexing.index(one)
                parent.append(initial)
            else:
                continue

        print(f'indexing : {indexing}')
        print(f'parent : {parent}')

        # f1과 f2를 합치기
        union(indexing.index(f1), indexing.index(f2))
        print(f'합친 후 : {parent}')

        # 합치고 나서 find로 업데이트
        find(indexing.index(f1))
        print(f'find({f1})의 값 : {find(indexing.index(f1))}')
        find(indexing.index(f2))
        print(f'find({f2})의 값 : {find(indexing.index(f2))}')

        print(f'찐찐 합친 후 : {parent}')
        print()

