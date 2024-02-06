def solution(cards1, cards2, goal):
    answer = ''
    c1 = 0
    c2 = 0
    find = 1
    for wr in goal:
        if c1 != len(cards1) and cards1[c1] == wr:
            c1 += 1
        elif c2 != len(cards2) and cards2[c2] == wr:
            c2 += 1
        else:
            answer = "No"
            find = 0
            break
            
    if find == 1:
        answer = "Yes"
    return answer