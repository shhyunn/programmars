#https://school.programmers.co.kr/learn/courses/30/lessons/12949.py
def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    
    for i0 in range(len(arr1)):
        for i1 in range(len(arr2[0])):
            sum = 0
            for i2 in range(len(arr2)):
                sum += arr1[i0][i2] * arr2[i2][i1]
            answer[i0][i1] = sum          
    return answer