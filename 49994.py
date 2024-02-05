#https://school.programmers.co.kr/learn/courses/30/lessons/49994.py
def solution(dirs):
    answer = 0
    remem = []
    x,y,nx, ny = 0,0,0, 0
    update = 0
    for k in dirs:
        update = 0
        
        if k == "U" and y < 5:
            nx,ny = x,y+1
            update = 1
        elif k == "D" and y > -5:
            nx,ny = x, y-1
            update = 1
        elif k == "R" and x < 5:
            nx, ny, update = x+1,y,1
        elif k == "L" and x > -5:
            nx, ny, update = x-1,y,1
        
        if [x,y,nx,ny] not in remem and update == 1:
            remem.append([x,y,nx,ny])
            remem.append([nx,ny,x,y])
            answer += 1
        x,y = nx,ny
        
    return answer

print(solution("ULURRDLLU"))