#https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = -1
    stt = []
    for ch in s:
        if stt and stt[-1] == ch:
            stt.pop()
        else:
            stt.append(ch)
    
    if stt:
        answer = 0
    else:
        answer = 1
    
    return answer

print(solution("baabaa"))