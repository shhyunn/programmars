      
def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)
    name_dic = {name:id for id,name in enumerate(enroll)}

    for sell,cnt in zip(seller,amount):
        curr = sell
        total = cnt*100
        while curr != "-":
            dic = int(total*0.1)
            if dic < 1:
                answer[name_dic[curr]] += total
                break
            else:
                answer[name_dic[curr]] += (total-dic)
            total = dic
            curr = referral[name_dic[curr]]
    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
              [2, 3, 5, 4]))