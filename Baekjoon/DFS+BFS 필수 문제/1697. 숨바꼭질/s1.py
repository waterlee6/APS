# 1697. 숨바꼭질

from collections import deque

n, k = map(int, input().split())  # n: 수빈이 위치, k: 동생 위치
q = deque()
q.append(n)              # 시작점 인큐하고 시작
visited = [0] * 100001   # 0부터 100,000까지이므로

while q:
    # 디큐하기
    i = q.popleft()

    # 종료조건
    if i == k:
        break

    # 인큐하기
    for j in [i+1, i-1, 2*i]:
        if 0 <= j <= 100000 and visited[j] == 0:
            q.append(j)
            visited[j] = visited[i]+1

print(visited[k])
