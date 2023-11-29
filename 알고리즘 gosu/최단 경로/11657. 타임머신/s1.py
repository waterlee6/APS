# 11657. 타임머신
'''
한 도시에서 다른 도시로 이동하는 최단 시간 구하기 -> 다익스트라?
가중치가 음수 혹은 0인 경우가 있음 -> 벨만포드 알고리즘!

1번 도시에서 나머지 도시로 가는 가장 짧은 시간을 출력
해당 도시로 가는 결과가 없으면 -1을 출력
어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면(=> 음의 사이클) -1 출력
'''

# 벨만 포드 알고리즘 구현 -> 음수 순환이 존재하면 True, 존재하지 않으면 False를 반환하는 함수
def bf(s):
    # 시작 노드에 대해서 초기화
    distance[s] = 0

    # 전체 n번의 라운드(round)를 반복
    for i in range(n):

        # 매 반복마다 모든 간선을 확인
        for j in range(m):
            now = routes[j][0]
            next = routes[j][1]
            cost = routes[j][2]

            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            # ★★★ distance[now] != inf 조건은 왜 필요한거지?
            if distance[now] != inf and distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost

                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재 (값이 갱신되어야만 두 번째 if문으로 들어올 수 있음)
                if i == n-1:
                    return True  # 음수 순환이 존재하면 True를 반환
    return False  # 음수 순환이 존재하지 않으면 False를 반환


import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n: 도시의 개수, m: 간선(버스노선)의 개수
s = 1  # 출발 노드
inf = int(1e9)

# 간선 정보를 받을 리스트 선언
routes = []
for _ in range(m):
    a, b, w = map(int, input().split())
    routes.append((a, b, w))  # a에서 b로 가는 시간이 w
# 최단 경로 테이블 선언
distance = [inf] * (n + 1)

# 1. 벨만 포드 알고리즘 실행하기
is_negative_cycle = bf(1)

# 2. 만약 음의 순환이 있다면 -1을 출력
if is_negative_cycle:
    ans = -1
    print(ans)

# 3. 음의 순환이 없다면 distance의 2번부터 n번까지를 출력
# (경로가 없을 경우에는 -1을 출력)
else:
    ans = []
    for i in range(2, n+1):
        if distance[i] != inf:
            ans.append(distance[i])
        else:
            ans.append(-1)
    print(*ans, sep='\n')
