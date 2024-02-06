# 단속카메라
'''
진입로를 기준으로 정렬하면 틀리는듯?
'''


def solution(routes):
    cnt = 0  # 카메라 개수를 셀 변수 선언
    positions = []  # 카메라 위치를 저장할 리스트

    # 1. routes를 오름차순으로 sort (진입로 기준 → 진입로 기준으로 하면 안되나벼...)
    routes.sort()
    # print(f'sorted_routes: {routes}')

    # 2. 처음 변수 설정
    camera = -60000  # 첫 카메라 설치 지점 (범위 외)
    latest_end = -60000  # 직전 route의 종료 지점을 저장할 변수

    # 3. route를 하나씩 돌며 조건에 맞게 카메라 위치 지정
    for route in routes:

        # 카메라가 이미 경로 내에 있으면 pass
        if route[0] <= camera and camera <= route[1]:
            latest_end = route[1]
            # print(f'{i}번 route를 두번째에서 건너뜀 {positions}')
            continue

        # 직전 종료 지점이 이번 종료 지점보다 뒤에 있다면 (피라미드식 반례) -> latest_end로 해결
        if latest_end > route[1]:
            camera = route[1]
            # cnt -= 1
            positions.pop()
            positions.append(camera)
            latest_end = route[1]
            # print(f'{i}번 route를 첫번째에서 제거하고 append {positions}')
            continue

        # 카메라가 경로 내에 없으면 제일 마지막 위치에 설치
        else:
            camera = route[1]
            positions.append(camera)
            cnt += 1
            latest_end = route[1]
            # print(f'{i}번 route를 세번째에서 append {positions}')

    answer = cnt
    return answer