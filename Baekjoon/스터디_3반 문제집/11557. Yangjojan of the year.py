T = int(input())
for tc in range(T):
    N = int(input())  # 테스트 케이스별 학교의 개수
    howmuch = 50  # 술 소비가 가장 많은 학교가 마신 양
    where = ''  # 술 소비가 가장 많은 학교의 이름

    for n in range(N):
        S, L = input().split()  # S: 학교의 이름, N: 술의 양
        L = int(L)  # 소비한 술의 양 정수로 바꿔주기
        # print(S, L)
        # print(type(S), type(L))

        if L > howmuch:
            howmuch = L
            where = S
        else:  # 자꾸 Ehwa가 떠서 continue 괜히 넣어봄...
            continue

    print(S)
