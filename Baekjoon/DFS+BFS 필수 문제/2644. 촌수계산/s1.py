# 2644. 촌수계산

n = int(input())  # n: 사람의 수
p1, p2 = map(int, input().split())
m = int(input())  # m: 관계의 개수
family = [[] for _ in range(n+1)]  # 부모 자식 관계를 기록할 리스트 (번호 맞추기 위해 +1)

for _ in range(m):
    x, y = map(int, input().split())  # x가 y의 부모
    family[x].append(y)  # 연결을 양방향으로 확인
    family[y].append(x)

## p1과 p2가 몇 칸 떨어져 있는지 세기 -> BFS
# 1. q, visited, 시작점
q = []
visited = [-1] * (n+1)

start = min(p1, p2)   # p1, p2 중 더 작은 값을 시작점, 더 큰 값을 end로 설정
end = max(p1, p2)

q.append(start)
visited[start] = 0

# 2. BFS 탐색하기
while q:
    # 2-1. 디큐하기
    i = q.pop(0)

    # 2-2. 인큐하기
    for j in family[i]:
        if visited[j] == -1:
            q.append(j)
            visited[j] = visited[i] + 1

print(visited[end])