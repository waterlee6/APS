def dfs(i, N, input_list):  #i: 현재 정점, N: 전체 정점의 개수, list: 탐색을 할 리스트
    #1. 변수 설정
    # n = len(input_list)  #n: 탐색할 리스트의 길이
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

N = 6
connect = [[], [2, 4], [1, 3, 6, 5], [4, 2], [1, 3], [2], [2]]
input_list = [5, 6]
print(dfs(2, N, input_list))
