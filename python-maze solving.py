def find_maze_path(maze):
    stack = [(mazestart, [mazestart])]  # 시작점 추가, 경로 리스트 추가
    xn = len(maze) #행개수
    yn = len(maze[1]) #열개수
    visited = set() #방문기록저장용기

    
    while stack:
        (x, y), path = stack.pop()  # 스택에서 위치와 경로 추출
        
        # 방문한 위치인 경우 continue
        if (x, y) in visited:
            continue
        visited.add((x, y)) #방문기록저장

        if x == mazeend[0] and y == mazeend[1]:  # 도착점인 경우
            global mazepath #경로 리스트를 전역 변수로 지정
            mazepath = path
            return True

        # 갈 수 있는 위치 스택에 추가
        if x+1 < xn and maze[x+1][y] == 1:
            stack.append((((x+1, y)), path+[(x+1, y)]))
        if x-1 >= 0 and maze[x-1][y] == 1:
            stack.append((((x-1, y)), path+[(x-1, y)]))
        if y+1 < yn and maze[x][y+1] == 1:
            stack.append((((x, y+1)), path+[(x, y+1)]))
        if y-1 >= 0 and maze[x][y-1] == 1:
            stack.append((((x, y-1)), path+[(x, y-1)]))

    return False  # 경로가 없는 경우

mazestart = (1,0)
mazeend = [3,5]
maze = [[0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]]

if find_maze_path(maze):
    print("미로를 찾았습니다.")
    print("경로 :", mazepath)
else:
    print("미로를 찾지 못했습니다.")
