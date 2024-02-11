def solution(record):
    answer = []
    sequence = []
    nick_dic = {}
    for strr in record:
        if strr.startswith("Enter"):
            _,id,nick = strr.split()
            nick_dic[id] = nick
            sequence.append([1,id])
            
        elif strr.startswith("Leave"):
            _,id = strr.split()
            sequence.append([2,id])
        
        elif strr.startswith("Change"):
            _,id,nick = strr.split()
            nick_dic[id] = nick
    
    for seq in sequence:
        num = seq[0]
        id = seq[1]
        if num == 1:
            answer.append(nick_dic[id]+"님이 들어왔습니다.")
        elif num == 2:
            answer.append(nick_dic[id]+"님이 나갔습니다.")
        
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))