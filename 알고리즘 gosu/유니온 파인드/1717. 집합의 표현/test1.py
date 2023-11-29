def find(a):
    # [종료조건] 대표 노드가 자기 자신이면 return
    if parent[a] == a:
        return parent[a]
    # [수행내용]
    parent[a] = find(parent[a])  # ★★★ 이 값이 return 되었을 때 받아줄 변수가 필요함
    return parent[a]

parent = [0, 1, 2, 1, 4, 5, 6, 6]
# parent = [0, 1, 2, 1, 4, 5, 1, 6]

print(find(7))
find(7)
print(parent)  # [0, 1, 2, 1, 4, 5, 1, 6] 아니 그럼 얘도 바뀌어야 하는 거 아니야?






'''
def find(a):
    # [종료조건] 대표 노드가 자기 자신이면 return
    if parent[a] == a:
        return parent[a]
    # [수행내용]
    find(parent[a])
'''