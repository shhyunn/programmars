#https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    ll =len(prices) #5
    answer = [0]*ll
    stack = [0]
    for i in range(1,ll): #i: 1,2,3,4
        #1,2,3,2,3
        if prices[stack[-1]] <= prices[i]: #1과 2 비교, 3하고 
            stack.append(i) #스택에 1 추가, 2추가
        else: #i가 3일 때 3보다 2가 작음
            while stack and prices[stack[-1]] > prices[i]: #3이 2보다 작아질 때까지, 2하고 2 비교 조건 x
                k = stack.pop()
                answer[k] = i-k #2 pop, answer[2] = 1
                #인덱스 차이만큼 저장
            stack.append(i)

    if stack:
        for r in stack:
            answer[r] = ll - r -1
                
    return answer

print(solution([1,2,3,2,3]))