# 13549. 숨바꼭질 3 (BFS로 풀기)
'''
직선 상에서 두 점의 위치가 주어짐
할 수 있는 일 : 앞으로 걷기(시간 1), 뒤로 걷기(시간 1), 앞으로만 2x위치로 이동(시간 0)
목적지까지 최단거리를 구하는 문제이기 때문에 BFS?

전체 가능한 점은 10만 개가 아니라 10만 1개!
now는 점의 인덱스 이므로 100,001이 될 수 없음 ∴ 등호는 제외, but 0은 될 수 있음

N > K인 경우 (수빈이가 동생보다 뒤에 있는 경우)에는 정답이 N-K가 된다.
순간이동은 N*2로 더 큰 수로만 갈 수 있으므로

deque(덱)을 import 하여 사용

visited 배열을 만들지 않고 time 배열만 사용해서 구할 수 있음 -> 더 직관적
'''
import sys
input = sys.stdin.readline
from collections import deque
N, K = map(int, input().split())  # N: 수빈이의 위치, K: 동생의 위치

# 1. visited, q, 시작점 인큐, 시작점 방문표시
# visited = [False] * MAX  # 방문한 점을 표시할 리스트
MAX = 100002             # 전체 가능한 점이 100,001개이므로 최댓값은 10만 2로 설정
time = [-1] * MAX        # 해당 점까지 도달하기 위해 걸린 최소 시간을 표시할 리스트 (-1이면 아직 방문하지 않았다는 뜻)

q = deque()
q.append(N)        # 수빈이의 위치를 인큐
time[N] = 0        # 수빈이 위치까지 걸린 시간은 0
min_time = 0       # 정답(가장 빠른 시간)을 담을 변수

# 2. N >= K 일 때
if N >= K:
    min_time = N - K

# 3. N < K 일 때 -> BFS
else:
    while q:   # q가 빌 때까지

        # 2-1. 디큐하기
        now = q.popleft()    # now: 현재 탐색중인 노드

        # 2-2. 종료 조건
        if now == K:
            break

        # 2-3. 탐색하기 (=> 인큐하기)
        # 순간이동
        if 0 <= now * 2 < MAX and time[now*2] == -1:
            q.appendleft(now*2)      # q의 가장 왼쪽에 삽입(가중치 0이므로)
            time[now*2] = time[now]  # now*2 점에 가기까지 걸린 시간은 지금까지의 시간과 동일

        # x-1 이동
        if 0 <= now - 1 < MAX and time[now-1] == -1:
            q.append(now-1)               # q의 오른쪽에 삽입
            time[now-1] = time[now] + 1   # now-1 점에 가기까지 걸린 시간은 지금까지의 시간 + 1

        # x+1 이동
        if 0 <= now + 1 < MAX and time[now+1] == -1:
            q.append(now+1)               # q의 오른쪽에 삽입
            time[now+1] = time[now] + 1   # now+1 점에 가기까지 걸린 시간은 지금까지의 시간 + 1

    min_time = time[K]

print(min_time)
