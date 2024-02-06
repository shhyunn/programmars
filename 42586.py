def solution(progresses, speeds):
    answer = []
    data = [100 - x for x in progresses]
    deploy = [num // div if num % div == 0 else num // div + 1 for num,div in zip(data, speeds)]
    temp = []
    cnt = 1
    for day in deploy:
        if len(temp) > 0:
            if temp[-1] >= day:
                cnt+=1
                continue
                
            else: #temp[-1]이 day보다 작다면
                temp.append(day)
                answer.append(cnt)
                cnt = 1
        else:
            temp.append(day)
    answer.append(cnt)
        
    return answer

print(solution([93, 30, 55],[1, 30, 5]))