# 1025. 제곱수 찾기

# 완전제곱수인지 판단하는 함수
def perfect(num):
    root = num ** (1/2)
    if root % 1 == 0:  # 제곱근이 정수이면
        return True
    else:
        return False


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

max_squarenum = -1  # 완전제곱수의 최대값을 저장할 변수

for i in range(N):
    for j in range(M):

        # 행의 공차 id는 -(N-1)부터 N-1까지 가능
        for id in range(-N+1, N):
            # 열의 공차 jd는 -(M-1)부터 M-1까지 가능
            for jd in range(-M+1, M):
                
                # id, jd 둘 다 0이면 제자리에서만 도므로 제외
                if id == jd == 0:
                    continue
                temp = ''  # 각 자리에서의 정수를 저장할 변수(각 공차에서 초기화)

                ni = i
                nj = j

                # 행 공차, 열 공차가 정해지면 범위 안에서 더해나가기
                while 0 <= ni <= N-1 and 0 <= nj <= M-1:
                    temp += str(arr[ni][nj])
                    ni += id
                    nj += jd
                    
                    # 각 temp가 완전제곱수인지 확인
                    num = int(temp)
                    if perfect(num):
                        if num > max_squarenum:
                            max_squarenum = num
                    else:
                        continue # jd for문을 탈출

print(max_squarenum)