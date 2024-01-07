# 2468. 안전 영역

import sys
input = sys.stdin.readline
from collections import deque

### input 받으며 최대 높이를 함께 저장하기
n = int(input())
arr = []
max_altitude = 0  # 최대 높이를 저장할 변수
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

    # 고도가 가장 높은 곳의 높이 찾기
    altitude = max(row)
    if max_altitude < altitude:
        max_altitude = altitude


### BFS + 델타탐색
dx = [0, 1, 0, -1]  # 우하좌상
dy = [1, 0, -1, 0]

max_zone = 0  # 안전영역의 최대 개수를 저장할 변수

# 1. rain만큼 비가 왔을 때 안전영역의 개수를 BFS로 탐색하기
# 비는 1 이상 max_altitued 미만으로 올 수 있음 (max_altitude이면 모두 물에 잠김)
for rain in range(1, max_altitude):

    zone = 0  # rain만큼 비가 왔을 때 안전영역의 개수를 저장할 변수
    visited = [[False] * n for _ in range(n)]
    q = deque()

    # 2. arr를 델타탐색으로 돌면서 시작점을 체크하기
    for i in range(n):
        for j in range(n):
            if arr[i][j] > rain and visited[i][j] == False:

                q.append((i, j))      # 시작점 인큐
                visited[i][j] = True  # 시작점 방문표시
                zone += 1             # 시작점을 새롭게 인큐할 때마다 zone을 +1

                # 3. BFS로 시작점과 연결된 지역들을 visited 표시
                while q:
                    # 디큐하기
                    x, y = q.popleft()

                    # 인큐하기
                    for d in range(4):  # 우하좌상 네 방향
                        nx, ny = x+dx[d], y+dy[d]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and arr[nx][ny] > rain:
                            q.append((nx, ny))
                            visited[nx][ny] = True

    # 4.다음 rain으로 넘어가기 전 max_zone 갱신하기
    if zone > max_zone:
        max_zone = zone

if max_zone == 0:  # 물에 잠긴 지역이 하나도 없으면 1을 출력
    print(1)
else:
    print(max_zone)