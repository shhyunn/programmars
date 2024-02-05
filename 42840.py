#https://school.programmers.co.kr/learn/courses/30/lessons/42840.py
def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    result = []
    
    for lst in [first, second, third]:
        cnt = 0
        temp = 0
        for ans in answers:
            if lst[cnt] == ans:
                temp += 1
            cnt += 1
            if cnt == len(lst):
                cnt = 0
            
        result.append(temp)
    
    max_value = max(result)
    
    for id in range(len(result)):
        if result[id] == max_value:
            answer.append(id+1)
            
    return answer

print(solution([1,2,3,4,5]))