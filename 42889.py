#https://school.programmers.co.kr/learn/courses/30/lessons/42889.py
def solution(N, stages):
    answer = [0]*N #스테이지 5개
    answer2 = [len(stages)]*N #8명
    for i in range(len(stages)): #8번 반복
        if stages[i]-1 == N:
            continue
            
        answer[stages[i]-1] += 1 #실패한 유저의 수
        for j in range(stages[i],N): 
            answer2[j] -= 1

    result = [0 for _ in range(N)]
    
    for i, (a,b) in enumerate(zip(answer, answer2)):
        if b == 0:
            result[i] = 0
        else:
            result[i] = a / b

    id = sorted(range(len(result)), key=lambda i: result[i], reverse=True)
    id = [i+1 for i in id]

    return id