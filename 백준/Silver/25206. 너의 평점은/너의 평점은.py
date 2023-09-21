# 25206. 너의 평점은

# import sys
# sys.stdin = open('input.txt')
N = 20
arr = []  # 학점과 평점이 들어갈 빈 리스트 선언
score = {  # 등급 변환표
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

# 등급이 'P'인 경우는 제외하고 arr 리스트에 학점/등급 넣기
for _ in range(N):
    sub = list(input().split())
    if sub[2] != 'P':
        arr.append(float(sub[1]))
        arr.append(score[sub[2]])
# print(arr)

# 전공평점 계산하기
# 학점, 등급 / 전공평점 = (학점 * 등급) / 학점의 총합
M = len(arr)
bunja = 0  # 학점 * 등급의 합
bunmo = 0  # 학점의 총합

for i in range(M//2):
    bunja += arr[i*2] * arr[i*2+1]
for i in range(M//2):
    bunmo += arr[i*2]

rst = bunja / bunmo
print(f'{rst:6f}')