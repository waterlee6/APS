# 이모티콘 할인행사

import itertools

def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)
    discounts = [0.1, 0.2, 0.3, 0.4]

    rates = list(itertools.product(discounts, repeat=m))  # 할인율 조합을 담을 리스트
    # print(rates)

    max_register = 0  # 전체 할인율에서 가입한 최대 인원
    max_sales = 0  # 전체 할인율에서 최대 매출액

    for rate in rates:  # 할인율 rate는 고정된 값
        # print('<<', rate, '>>')
        register = 0  # 이 할인율에서 서비스에 가입한 인원
        sales = 0  # 이 할인율에서 최대 매출액

        for user in users:
            user_cost = 0  # 한 명의 유저가 지불할 최대 금액

            for i in range(m):  # 이모티콘의 갯수만큼 순회

                # 구매하지 않는 경우
                if user[0] / 100 > rate[i]:
                    continue

                # 구매하는 경우
                else:
                    cost = emoticons[i] * (1 - rate[i])
                    user_cost += cost

                # 유저의 예산을 초과하는 경우 -> 서비스 등록하고 break
                if user_cost >= user[1]:
                    register += 1
                    user_cost = 0
                    break

            # 모든 이모티콘을 확인했을 때 유저의 예산을 초과하지 않는 경우 -> 매출액에 포함
            if user_cost > 0:
                sales += user_cost

        # 모든 유저를 확인한 후, 이 할인율에서의 가입자 수와 매출액 확인
        if register > max_register:
            max_register = register
            max_sales = sales  # ★★★
        if register == max_register and max_sales < sales:
            max_sales = sales

    # 정답 출력
    answer = [max_register, max_sales]
    return answer