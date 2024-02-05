#https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    lst = list(s)
    dict = {"[":"]","{":"}","(":")"}
    
    for i in range(len(s)):
        delete_lst = []
        solve = 1
        if i != 0:
            ch = lst.pop(0)
            lst.append(ch)

        for c in lst:   
            if c in ["]","}",")"]:
                if len(delete_lst) == 0:
                    solve = 0
                    continue
                a = delete_lst.pop()
                
                if c == dict[a]:
                    
                    continue
                else:
                    solve = 0
                    continue
            else:
                delete_lst.append(c)
                
        if solve == 1 and len(delete_lst) == 0:
            answer += 1
        
    return answer

print(solution("(){}[]"))