# 2908. 상수

a, b = input().split()

# 주어진 수를 거꾸로 바꾸기
new_a = ''
new_b = ''
for i in range(2, -1, -1):  # 두 수는 세 자리 수라고 했으므로
    new_a += a[i]
    new_b += b[i]

print(max(int(new_a), int(new_b)))