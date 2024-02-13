def solution(n,a,b):
    answer = 1
    lst = [0]*n+[i for i in range(1,n+1)]
    while n != 1:
        for i in range(n,2*n,2): #8,10,12,14 // 
            if (lst[i] == a and lst[i+1] == b) or (lst[i] == b and lst[i] == a):
                return answer
            elif lst[i] == a or lst[i] == b:
                lst[i//2] = lst[i]
            else:
                lst[i//2] = lst[i+1]
        answer += 1
        n //= 2 #n은 4가 됨 -> n은 2가 됨
    return answer

print(solution(2,1,2))

'''
answer = 0
while a != b:
    a = (a+1)//2
    b = (b+1)//2
    answer += 1
'''