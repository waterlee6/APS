# 2667. 단지번호붙이기
'''
델타로 돌면서, 1이 걸리면 거기서 BFS 탐색하기

델타 탐색 돌면서 인큐할 때에 값을 바꿔주면 시작점의 값은 바뀌지 않는 문제 발생
시작점이 다른 집과 연결되어 있으면 언젠가 바뀌지만, 
집이 한 칸씩 떨어져 있는 경우에는 바뀌지 않음
디큐할 때에 시작점 값도 바꿔주는 것으로 해결
'''

arr = []
N = int(input())
for _ in range(N):
    str_line = ' '.join(input())
    arr.append(list(map(int, str_line.split())))
# print(arr)

# 1. 델타탐색으로 돌기
dx = [0, 1, 0, -1]  # 우하좌상
dy = [1, 0, -1, 0]
cnt = -1  # 단지를 구분할 flag

for i in range(N):
    for j in range(N):

        # 2. 1인 칸을 만나면 그 칸에서부터 BFS 돌기
        if arr[i][j] == 1:
            cnt += 1  # 이전 단지와 다른 단지임을 구분
            q = [(i, j)]  # BFS위한 q (visited는 필요 X, 바로 arr에 표시)
            while q:
                # 2-1. 디큐하기
                x, y = q.pop(0)
                arr[x][y] = 10 + cnt  # ★★★ 

                # 2-2. 인큐하기
                for d in range(4):  # 동서남북 4방향
                    nx, ny = x+dx[d], y+dy[d]
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                        q.append((nx, ny))
                        arr[nx][ny] = 10 + cnt
# print(arr)
# print(cnt)

# 3. cnt별 집의 수 출력하기
ans = [0 for _ in range(cnt+1)]

for row in arr:
    for n in range(cnt+1):
        ans[n] += row.count(n+10)

print(cnt+1)
ans.sort()
print(*ans, sep='\n')
