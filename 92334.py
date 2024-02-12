def solution(id_list, report, k):
    answer = [0]*len(id_list)
    id_dic={name:i for i,name in enumerate(id_list)}
    count_dic={name:[] for name in id_list} #name은 신고 당한 사람. 그 안의 리스트는 그 사람을 신고한 name
    for strr in report:
        name1, name2 = strr.split()
        count_dic[name2].append(name1) #신고한 사람 추가
    
    for name in id_list:
        count_dic[name] = list(set(count_dic[name]))
        if len(count_dic[name]) >= k:
            for name2 in count_dic[name]:
                answer[id_dic[name2]]+=1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))