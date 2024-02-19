def solution(maps):
    row,col = len(maps),len(maps[0])
    visited = [[[0 for _ in range(2)] for _ in range(col)] for _ in range(row)]
    
    queue = []
    y = [-1,1,0,0]
    x = [0,0,-1,1]
    end_y,end_x = -1,-1
    for i in range(row):
        for j in range(col):
            if maps[i][j] == "S":
                queue.append((i,j,0,0))
                visited[i][j][0] = 1
            if maps[i][j] == "E":
                end_y,end_x = i,j

    while queue:
        j,i,k,l = queue.pop(0)
        if j == end_y and i == end_x and l == 1:
            return k

        for n in range(4): #반복문 자체에서 l이 초기화가 안됨
            cx = i + x[n]
            cy = j + y[n]

            if not(0 <= cy < row and 0 <= cx < col and maps[cy][cx] != "X"):
                continue

            if maps[cy][cx] == "L": #레버일 경우
                if not visited[cy][cx][1]:#레버일 때의 그곳을 방문하지 않았을 경우
                    visited[cy][cx][1] = 1 #방문으로 설정
                    queue.append((cy,cx,k+1,1))
            else:           
                if not visited[cy][cx][l]: #레버가 아닐 경우
                    visited[cy][cx][l] = 1
                    queue.append((cy,cx,k+1,l))
    return -1

'''
if maps[cy][cx] == "L":
    l = 1

if not visited[cy][cx][l]:
    visited[cy][cx][l] = 1
    queue.append((cy,cx,k+1,l))
'''
    
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))

# from collections import deque

# def is_valid_move(ny,nx,n,m,maps):
#     return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X"

# def append_to_queue(ny,nx,k,time,visited,q):
#     if not visited[ny][nx][k]:
#         visited[ny][nx][k] = True
#         q.append((ny,nx,k,time+1))

# def solution(maps):
#     n,m = len(maps),len(maps[0])
    
#     visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
#     dy = [-1,1,0,0]
#     dx = [0,0,-1,1]
#     q = deque()
#     end_y, end_x = -1,-1
    
#     for i in range(n):
#         for j in range(m):
#             if maps[i][j] == "S":
#                 q.append((i,j,0,0))
#                 visited[i][j][0] = True
#             if maps[i][j] == "E":
#                 end_y, end_x = i,j
#     while q:
#         y,x,k,time = q.popleft()
        
#         if y == end_y and x == end_x and k == 1:
#             return time
        
#         for i in range(4):
#             ny,nx = y + dy[i], x + dx[i]
#             if not is_valid_move(ny,nx,n,m,maps):
#                 continue
            
#             if maps[ny][nx] == "L":
#                 append_to_queue(ny,nx,1,time,visited,q)
#             else:
#                 append_to_queue(ny,nx,k,time,visited,q)
#     return -1