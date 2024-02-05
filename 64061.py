#https://school.programmers.co.kr/learn/courses/30/lessons/64061.py
# def solution(board, moves):
#     answer = 0
#     last = []
#     bag = []
    
#     for i in range(len(board)):
#         for j in range(len(board)):
#             if board[j][i] != 0:
#                 last.append(j)
#                 break
                
#         if len(last) < i+1:
#             last.append(0)
    
#     for mov in moves:
#         if last[mov-1] != len(board):
#             bag.append(board[last[mov-1]][mov-1])
#             last[mov-1] += 1
#             if len(bag)>=2 and bag[-1] == bag[-2]:
#                     bag.pop()
#                     bag.pop()
#                     answer += 2 
#     return answer

def solution(board, moves):
    answer = 0
    bag = []
    
    for mov in moves:
        for i in range(len(board)):     
            if board[i][mov-1] != 0:
                bag.append(board[i][mov-1])
                board[i][mov-1] = 0

                if len(bag)>=2 and bag[-1] == bag[-2]:
                    bag.pop()
                    bag.pop()
                    answer += 2 

                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))