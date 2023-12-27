# 택배 배달과 수거하기 (풀이 참고해 정답)

'''
* cap: 박스 최대 개수, n: 배달할 집의 개수, deliveries: 배달 리스트, pickups: 수거 리스트
* 모든 배달과 수거를 마치고 물류창고로 돌아오는 최소 이동 거리

물류창고 위치 : 0
현재 위치 : p, 현재 짐의 개수 on_truck
현재 위치에서 n번째 집으로 이동할 때 거리 = ans(n - p)

알단 먼 곳부터 한 번에 해결하기?
for문 안에 while문이 들어가는 구조로 해결
for문으로 제일 먼 곳 -> 가까운 곳으로 이동,
while문으로 각각의 집에 대해 배달을 마무리

while문 도는 동안에 drop_left나 pick_left가 남아 있다면 중간 지점도 처리 가능?

'''
def solution(cap, n, deliveries, pickups):
    # 집 번호와 맞추기 위해 리스트 왼쪽에 0 삽입
    drops = [0]
    drops.extend(deliveries)  # [0, 1, 0, 3, 1, 2]
    picks = [0]
    picks.extend(pickups)     # [0, 0, 3, 0, 4, 0]

    # 변수 설정
    total_dist = 0   # 총 이동거리
    drop_left = 0    # i번 집의 남은 배달 개수
    pick_left = 0    # i번 집의 남은 수거 개수

    # while문 다 돌면 다음 집으로의 이동은 for문을 통해 이루어짐
    # ★마지막까지 가서 내려놓고 싣고 오는 건 알겠는데, 처음에 갈 때 그럼 몇 개를 싣고 가야 돼? 무조건 cap 만큼 싣는다고 가정?? 처음에 몇 개를 싣는지 모르겠음...

    # 가장 마지막 집(n번째) 부터 1번째 집까지 돌기
    for i in range(n, 0, -1):

        # 해당 위치의 배달/수거 개수 입력
        drop_left += drops[i]
        pick_left += picks[i]

        # i번째 집에 drop 하거나 pcik 할 물건이 하나라도 남아 있으면 재방문 해야함
        while drop_left > 0 or pick_left > 0:
            total_dist += i    # while문 돌 때마다 i까지 오는데 소요한 거리 더하기
            drop_left -= cap   # 배달 수량 제거
            pick_left -= cap   # cap만큼 픽업 가능

        # i번째 집 배달/수거를 마치면 while문을 탈출 -> 이 시점에 아직 트럭에 자리가 남아 있다면 가는 길에 더 실어도 되지 않나?

    answer = total_dist * 2
    return answer