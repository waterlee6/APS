# 13549. 숨바꼭질 3 (BFS로 풀기)
'''
직선 상에서 두 점의 위치가 주어짐
할 수 있는 일 : 앞으로 걷기(시간 1), 뒤로 걷기(시간 1), 앞으로만 2x위치로 이동(시간 0)
목적지까지 최단거리를 구하는 문제이기 때문에 BFS?

visited = False 조건은 왜 넣는거지?
전체 가능한 점은 10만 개가 아니라 10만 1개!
now는 점의 인덱스 이므로 100,001이 될 수 없음 ∴ 등호는 제외, but 0은 될 수 있음
'''

from collections import deque

N, K = map(int, input().split())  # N: 수빈이의 위치, K: 동생의 위치

# 1. visited, q, 시작점 인큐, 시작점 방문표시
MAX = 100001   # 전체 가능한 점이 100,001개임
visited = [False] * MAX  # 방문한 점을 표시할 리스트
time = [0] * MAX         # 해당 점까지 도달하기 위해 걸린 최소 시간을 표시할 리스트

q = deque()
q.append(N)        # 수빈이의 위치를 인큐
time[N] = 0        # 수빈이 위치까지 걸린 시간은 0
visited[N] = True  # 수빈이 위치 방문표시

# 2. BFS 탐색
while q:   # q가 빌 때까지

    # 2-1. 디큐하기
    now = q.popleft()    # now: 현재 탐색중인 노드

    # 2-2. 탐색하기
    # 순간이동
    if now * 2 < MAX and visited[now*2] == False:
        q.appendleft(now*2)      # q의 가장 왼쪽에 삽입(가중치 0이므로)
        visited[now*2] = True    # 방문표시
        time[now*2] = time[now]  # now*2 점에 가기까지 걸린 시간은 지금까지의 시간과 동일

    # x+1 이동
    if now + 1 < MAX and visited[now+1] == False:
        q.append(now+1)               # q의 오른쪽에 삽입
        visited[now+1] = True         # 방문표시
        time[now+1] = time[now] + 1   # now+1 점에 가기까지 걸린 시간은 지금까지의 시간 + 1

    # x-1 이동
    if now - 1 >= 0 and visited[now-1] == False:
        q.append(now-1)               # q의 오른쪽에 삽입
        visited[now-1] = True         # 방문표시
        time[now-1] = time[now] + 1   # now-1 점에 가기까지 걸린 시간은 지금까지의 시간 + 1

    # 가지치기
    if now == K:
        break

print(time[K])


