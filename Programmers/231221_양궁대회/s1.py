'''
배열의 i번째 원소는 과녁의 10-i 점을 맞힌 화살 개수
가장 큰 점수 차로 우승할 수 있는 경우가 정답
정답이 여러 개인 경우 낮은 점수를 많이 맞힌 순으로 return 
* 가장 높은 총점 획득 -> 높은 점수부터 채우기
* 같은 총점일 때는 낮은 점수 많이 맞힌 순 -> 낮은 점수부터 채우기 

for문을 돌면서 큰 점수부터 차례로 가져가는 건 가능
while문으로 큰 점수를 포기하고 작은 점수를 가져가는 경우를 반복해야 하는데, 종료조건과 큰 점수를 어떻게 포기할 것인지를 모르겠음
1. while문 돌면서 인덱스를 하나씩 증가시키기 -> 예를 들어 0번째는 라이언이 가져가고, 1번째는 포기, 2번째는 가져가는 경우를 포함하지 못함
2. info에서 가장 숫자가 큰 것부터 포기하기? 

내가 봤을 땐 완탐으로 풀어야 할 듯... 
인터넷 풀이 참고하니 BFS로 푼 경우가 많네 

라이언이 info의 각 원소에 대해 선택할 수 있는 경우의 수는 쏘거나/안 쏘거나
쏘는 경우에는 어피치보다 1점만 높으면 되니까 info[i]+1

23번 테케는 라이언과 어피치가 비기는 경우 
'''
import itertools

def solution(n, info):
    
    
    # 낮은 점수가 많은 배열을 찾는 함수
    def find_lowest(arrows):
        global answer
        
        if len(arrows) == 0:
            answer = [-1]
        elif len(arrows) == 1:
            answer = arrows[0]
        else:
            max_cnt = -110
            for arrow in arrows:
                cnt = 0
                for i in range(10, -1, -1):
                    # 0이 나오면 -10
                    if arrow[i] == 0:
                        cnt -=10
                    # 0이 아닌 수가 나오면 더하고 반복 중단
                    else:
                        cnt += arrow[i]
                        break
                if cnt > max_cnt:
                    max_cnt = cnt
                    answer = arrow
        return answer
    
        
    # 1. 쏘기/안쏘기 모든 경우의 수 구하기 (0점은 고려 X)
    # [True, False]의 중복순열로 구하기
    yesno = [True, False]
    pers = list(itertools.product(yesno, repeat=10))
    # print(pers[0])  # (True, True, True, True, True, True, True, True, True, True, True)
    # print(pers[1])  # (True, True, True, True, True, True, True, True, True, True, False)
    # print(pers[2])  # (True, True, True, True, True, True, True, True, True, False, True)
    
    max_gap = 0     # 점수 차의 최대값
    arrows = []     # 점수 차가 최대일때의 arr를 append할 리스트
    
    # 2. 경우의 수(pers)를 모두 돌며 조건을 만족하는 경우를 arrows에 담기
    for per in pers:
        a_score = 0      # 어피치의 총점
        l_score = 0      # 라이언의 총점
        arr = [0] * 11   # 라이언이 쏠 화살 개수
        left = n         # 라이언의 남은 화살 개수
        check = True     # 화살이 부족한지 판단할 플래그
        
        for i in range(10):  # 0점 일때는 고려하지 않음 
            
            # 2-1. i점 과녁이 True = 라이언이 먹어야!
            if per[i]:
                
                # 쏠 수 있는 경우(화살 남아있음)
                if left > info[i]:
                    left -= info[i]+1 
                    l_score += 10-i
                    arr[i] = info[i]+1
                
                # 쏠 수 없는 경우(화살이 부족)
                else:
                    check = False
                    break  # i for문 break -> 다음 per로
                    
            
            # 2-2. i점 과녁이 False = 어피치가 먹어야!
            else:
                if info[i]:
                    a_score += 10-i
                    
        # 2-3. check == True : i for문을 끝까지 다 돌고 옴 
        if check:
            
            # 주어진 화살 n개는 다 소비해야 하므로 0점에 남은 화살 다 넣기
            if left != 0:
                arr[10] = left
            
            gap = l_score - a_score
            
            # gap > max_gap 일때는 기존의 arrows를 초기화 해야 함
            if gap > max_gap :
                max_gap = gap
                arrows.clear()
                arrows.append(arr)
                
            # gap == max_gap 일때는 arrows에 append만 ★★★ 라이언과 어피치가 동점인 경우 제외시키기 
            elif gap == max_gap and gap != 0:
                max_gap = gap
                arrows.append(arr)
    # print(max_gap, arrows)
    
    # 3. 정답 출력
    find_lowest(arrows)
        
    return answer