# 1991. 트리 순회

'''
트리를 어떻게 만들 것인가가 문제
-> 부모노드와 자식노드가 순서대로 주어지고 있으므로
딕셔너리를 이용해 만드는 것이 가장 편리
https://kill-xxx.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-1991%EB%B2%88-%ED%8A%B8%EB%A6%AC-%EC%88%9C%ED%9A%8C-%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98%EC%99%80-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC-%EC%9D%B4%EC%9A%A9%ED%95%98%EA%B8%B0
'''

# 1. 트리의 정보를 딕셔너리로 받기
N = int(input())  # N: 노드의 개수
data = {}  # 트리의 정보를 담을 빈 딕셔너리 선언
for _ in range(N):
    root, left, right = input().split()
    data[root] = left, right
# print(data)

# 2. 전위순회 (부모 -> 좌 -> 우)
def preorder(v):  # v: 현재 탐색중인 노드
    if v != '.':
        print(v, end='')      # 현재 노드 기록
        preorder(data[v][0])  # 왼쪽 노드 탐색
        preorder(data[v][1])  # 오른쪽 노드 탐색

# 3. 중위순회 (좌 -> 부모 -> 우)
def inorder(v):
    if v != '.':
        inorder(data[v][0])   # 왼쪽 노드 탐색
        print(v, end='')      # 현재 노드 기록
        inorder(data[v][1])   # 오른쪽 노드 탐색

# 4. 후위순회 (좌 -> 우 -> 부모)
def postorder(v):
    if v != '.':
        postorder(data[v][0])  # 왼쪽 노드 탐색
        postorder(data[v][1])  # 오른쪽 노드 탐색
        print(v, end='')       # 현재 노드 기록

# 5. 결과 출력하기
preorder('A')
print('')
inorder('A')
print('')
postorder('A')