# 이모티콘 할인행사 (도전하다가 실패한 코드)

'''
users = [[비율, 가격], [비율, 가격], ...]
emoticons = [정가, 정가, ...]
이모티콘 서비스 가입 수와 이모티콘 매출액을 1차원 정수 배열에 담아 return

조건 1. 이모티콘 서비스 가입 수 최대
조건 2. 이모티콘 판매액 최대

할인율 4개, 유저 수 100명, 이모티콘 개수 7개로 4 * 100 * 7 = 2800 밖에 안되니까 완탐?
'''


def solution(users, emoticons):
    # print(users)      # [[40, 10000], [25, 10000]]
    # print(emoticons)  # [7000, 9000]

    discounts = [0.1, 0.2, 0.3, 0.4]

    # 서비스에 가입한 경우 중 최대 값을 뽑기
    temp_price = 0
    ans1 = 0  # 최종 서비스 가입자 수
    ans2 = 0  # 최종 이모티콘 매출액

    # 각 유저 별로 서비스 가입자가 가장 많은 할인율을 결정 -> 각 유저는 별개의 사건?
    rst = []

    for user in users:
        cost = 0  # 이모티콘 구입에 사용한 비용
        register = False

        for emo in emoticons:

            for rate in discounts:

                # 구매하지 않는 경우
                if user[0] / 100 > rate:
                    continue  # 다음 할인율으로

                # 구매하는 경우
                # 매출액을 최대로 해야 하므로 더 저렴한 할인율을 제공할 필요는 없음
                else:
                    cost += emo * rate
                    break  # 다음 이모티콘으로

            # 기준보다 넘어가면 서비스 가입
            if cost >= user[1]:
                register = True
                cost = 0
                rst.append([register, cost])
                break  # 다음 user로

        # 중간에 break하지 않고 모든 이모티콘을 구매한 경우 cost 기록
        rst.append([register, cost])

    print(rst)
    summary = 0
    for r in rst:
        if r[0] == False:
            summary += r[1]
    print(summary)

    answer = []
    return answer