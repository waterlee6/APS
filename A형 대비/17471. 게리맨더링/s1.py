#17471. 게리맨더링

#DFS 탐색하는 함수
#DFS 탐색해서 하나라도 못 가는 지역이 있으면 바로 그만두기
def dfs(i, N, input_list):  #i: 현재 정점, N: 전체 정점의 개수, list: 탐색을 할 리스트
    #1. 변수 설정
    stack = []  #빈 스택 선언
    visited = [0] * (N+1)  #visited 선언
    visited[i] = 1
    # stack.append(i)

    #2. 탐색 시작
    while True:
        for j in range(1, N+1):
            if visited[j] == 0 and j in input_list and j in connect[i]:
                # print(j)
                stack.append(i)  #★stack에 i 더하고(j를 더하면 잘못된 값이 나옴)
                visited[j] = 1   #j에 방문표시하고
                i = j            #탐색 정점을 j로 변경
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
    return(visited)


import sys
sys.stdin = open('input.txt')
N = int(input())  #N: 구역의 개수
data = [0] + list(map(int, input().split()))  #각 지역 인구수(인덱스 맞추기 위해 0번 추가)
connect = [[]]  #구역간 연결을 나타낼 인접리스트

#1. 인접리스트 구하기
for n in range(N):
    a = list(map(int, input().split()))
    a.pop(0)
    connect.append(a)
# print(connect)  #[[], [2, 4], [1, 3, 6, 5], [4, 2], [1, 3], [2], [2]]


#2. 1~N번 지역을 부분집합으로 나누기
area = [i for i in range(1, N+1)]  #1번부터 N번까지의 지역구
for i in range(1, 1<<(N-1)):  #공집합 제외, 중복되는 경우 제외
    g1 = []
    g2 = []
    for j in range(N):
        if i & (1<<j):
            g1.append(area[j])
        else:
            g2.append(area[j])
    # print(g1, g2)


    #3. 각 부분집합(g1, g2)에서 DFS 탐색 -> 부분집합 지역구들이 연결되어 있는지 확인
    g1_ppl = 0  #g1 지역의 인구수 계산할 변수
    g2_ppl = 0  #g2 지역의 인구수 계산할 변수
    check = True
    '''
    한 점만 찍어서 DFS 돌리면, 연결되어 있다면 다 가는거 아닌가?
    '''
    #3-1. g1에서 먼저 탐색하기
    i1 = g1[0]  #탐색을 시작할 위치 i1은 g1의 가장 첫 요소
    if sum(dfs(i1, N, g1)) == len(g1):  #visited개수가 g1의 길이와 같다면,
                                        #g1의 모든 요소를 탐색한 것이므로 가능한 방법
        for g in g1:
            g1_ppl += data[g]
    else:
        check = False  #g1이 탐색 불가능한 경우일 때 판단할 플래그

    #3-2. g1이 가능한 경우일 때, g2에서도 탐색
    i2 = g2[0]
    if check == True:
        if sum(dfs(i2, N, g2)) == len(g2):
            for g in g2:
                g2_ppl += data[g]
    else:
        continue  #다음 i로 탐색 넘어감

    print(g1, g2)




