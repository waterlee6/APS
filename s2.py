# 1283. 단축키 지정

N = int(input())  # N: 옵션의 개수
options = []
for _ in range(N):
    options.append(input())
# print(options)  # ['New', 'Open', 'Save', 'Save As', 'Save All']
used = []        # 이미 단축키로 지정된 알파벳을 담을 리스트


for i in range(N):  # 전체 options를 순회하기
    words = list(options[i].split())
    option = options[i]
    # print(words)   # ['New'], ['Open'], ['Save'], ['Save', 'As'], ['Save', 'All']
    # print(option)  # New, Open, Save, Save As, Save All

    # 1. 각 단어의 첫 글자만 검사하기
    for word in words:
        if word[0].lower() not in used:                 # 첫 글자가 아직 사용되지 않았으면
            used.append(word[0].lower())                # 단축키 지정한 알파벳을 소문자로 used에 저장
            new_word = '[' + word[0] + ']' + word[1:]   # word[0] 문자의 앞뒤에 [] 삽입
            words[words.index(word)] = new_word         # option에서 word가 위치한 인덱스를 찾아 word를 new_word로 교체
            options[i] = ' '.join(words)
            break  # 교체하면 word for문 탈출
        else:
            continue

    # 2. 왼쪽부터 차례대로 탐색하기
    # 1번 form문에서 break되지 않았다 -> 단어의 첫 글자는 이미 사용되었다
    else:
        length = len(option)
        for j in range(length):  # 해당 옵션의 길이만큼(공백도 포함) 순회하기
            if option[j].lower() not in used and option[j] != ' ':              # 사용되지 않았고 공백이 아니라면
                used.append(option[j].lower())                                  # 사용한 알파벳을 소문자로 used에 저장
                new_option = option[:j] + '[' + option[j] + ']' + option[j+1:]  # j번째 문자의 앞뒤에 [] 삽입
                options[i] = new_option                                         # options의 i번째를 new_option으로 바꾸기
                break  # 하나를 바꾸면 j for문을 빠져나오기
            else:
                continue  # 이미 사용한 글자이거나 공백이면 다음 글자로 넘어가기

for ans in options:
    print(ans)
