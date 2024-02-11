
def solution(participant, completion):
    dic = {key:0 for key in participant}
    
    for name in participant:
        dic[name] += 1
        
    for name in completion:
        dic[name] -= 1
        
    for name in dic.keys():
        if dic[name] > 0:
            return name