# 숫자 n의 약수를 구하기
# 약수의 합과 n이 같은지 판단하기

# n의 약수를 구하는 식 만들기
def prime(n):
    subnum = []

    for i in range(1, n):  # 자기 자신은 포함하지 않으므로 n까지만
        if n % i == 0:  # i가 n의 약수인 경우
            subnum.append(i)
            # continue도 필요 없음
            # i가 n의 약수가 아닌 경우에는 아무것도 안 해도 됨
    return subnum

while True:
    n = int(input())
    if n == -1:
        break
    else:
        # 출력 1안: print 함수 사용하기
        if sum(prime(n)) == n:
            print(n, end = ' = ')
            print(*prime(n), sep = ' + ')
        else:
            print(f'{n} is NOT perfect.')

        # 출력 2안: join 메서드 사용하기
        # ★ sep = ''를 안 넣으면 출력 형식이 틀렸다고 나오는데 무슨 차이지?
        if sum(prime(n)) == n:
            print(n, ' = ', ' + '.join(str(i) for i in prime(n)), sep = '')
        else:
            print(f'{n} is NOT perfect.')
