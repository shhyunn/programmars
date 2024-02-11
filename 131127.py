def solution(want, number, discount):
    #want는 원하는 물품 배열
    #제품 수량
    #discounter은 물품 배열
    origin = {key:value for key,value in zip(want, number)}
    answer = 0
    for i in range(len(discount)-10+1):
        dic = origin.copy()
        for j in range(i,i+10):
            cot = discount[j]
            if cot in dic.keys() and dic[cot] > 0:
                dic[cot] -= 1
            if all(value == 0 for value in dic.values()):
                answer += 1
                break
    
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))