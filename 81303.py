# #https://school.programmers.co.kr/learn/courses/30/lessons/81303.py
# def solution(n, k, cmd):
#     answer = ['O']*n
#     stack = [i for i in range(n)]
#     remove = []

#     for strr in cmd:
#         if len(strr) >= 3:
#             ch, n = strr.split()
#             n = int(n)
#             if ch == "D":
#                 k += n
#             elif ch == "U":
#                 k -= n
        
#         else:
#             ch = strr
#             if ch == "C":
#                 if stack[-1] == stack[k]:
#                     temp = stack[k]
#                     stack.remove(temp)
#                     remove.append(temp)
#                     k -= 1
#                 else:
#                     temp = stack[k]
#                     stack.remove(temp)
#                     remove.append(temp)
            
#             elif ch == "Z":
#                 ins = remove.pop()
#                 #print(stack)
#                 insert = 0
#                 for id, val in enumerate(stack):
#                     if ins < val: #작으면 삽입
#                         insert = 1
#                         if id <= k:#현재 삽입하려는 id
#                             stack.insert(id,ins)
#                             k+=1
#                         else: #현재 삽입하려는 id가 k보다 크다면..
#                             stack.insert(id,ins)
#                         break
                
#                 if insert == 0:
#                     stack.append(ins)
        
#     for id in remove:
#         answer[id] = "X"
#     answer = "".join(answer)

#     return answer

#     answer = ['O']*n
#     stack = [i for i in range(n)]
#     remove = []

#     for strr in cmd:
#         if len(strr) >= 3:
#             ch, n = strr.split()
#             n = int(n)
#             if ch == "D":
#                 k += n
#             elif ch == "U":
#                 k -= n
        
#         else:
#             ch = strr
#             if ch == "C":
#                 if stack[-1] == stack[k]:
#                     temp = stack[k]
#                     stack.remove(temp)
#                     remove.append(temp)
#                     k -= 1
#                 else:
#                     temp = stack[k]
#                     stack.remove(temp)
#                     remove.append(temp)
            
#             elif ch == "Z":
#                 ins = remove.pop()
#                 #print(stack)
#                 insert = 0
#                 for id, val in enumerate(stack):
#                     if ins < val: #작으면 삽입
#                         insert = 1
#                         if id <= k:#현재 삽입하려는 id
#                             stack.insert(id,ins)
#                             k+=1
#                         else: #현재 삽입하려는 id가 k보다 크다면..
#                             stack.insert(id,ins)
#                         break
                
#                 if insert == 0:
#                     stack.append(ins)
        
#     for id in remove:
#         answer[id] = "X"
#     answer = "".join(answer)

#     return answer

def solution(n, k, cmd):
    answer = ['O']*n
    remove = []
    #linked list, 가상 공간 도입
    up = [i-1 for i in range(n+2)]
    down = [i + 1 for i in range(n+1)]

    k+=1

    for strr in cmd:
        if len(strr) >= 3:
            ch, nn = strr.split()
            if ch == "D":
                for _ in range(int(nn)):
                    k = down[k]
            elif ch == "U":
                for _ in range(int(nn)):
                    k = up[k]
        
        else:
            ch = strr
            if ch == "C":
                remove.append(k)
                up[down[k]] = up[k]
                down[up[k]] = down[k]
                k = up[k] if n < down[k] else down[k]
            
            elif ch == "Z":
                ins = remove.pop()
                down[up[ins]] = ins
                up[down[ins]] = ins
        
    for id in remove:
        answer[id-1] = "X"
    answer = "".join(answer)

    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))