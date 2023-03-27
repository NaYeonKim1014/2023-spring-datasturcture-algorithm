def find_maze_path(maze):
    stack = [(mazestart, [mazestart])]  # add starting point, add route list
    xn = len(maze) # Number of rows
    yn = len(maze[1]) # Number of columns
    visited = set() # Save visit history set

    
    while stack:
        (x, y), path = stack.pop()  # Extracting Locations and Paths from stack
        
        # Continue if where visited
        if (x, y) in visited:
            continue
        visited.add((x, y)) # Save Visit History

        if x == mazeend[0] and y == mazeend[1]:  # if it's the arrival point
            global mazepath # Set route list as global variable
            mazepath = path
            return True

        # Add to stack where can go
        if x+1 < xn and maze[x+1][y] == 1:
            stack.append((((x+1, y)), path+[(x+1, y)]))
        if x-1 >= 0 and maze[x-1][y] == 1:
            stack.append((((x-1, y)), path+[(x-1, y)]))
        if y+1 < yn and maze[x][y+1] == 1:
            stack.append((((x, y+1)), path+[(x, y+1)]))
        if y-1 >= 0 and maze[x][y-1] == 1:
            stack.append((((x, y-1)), path+[(x, y-1)]))

    return False  # If there is no path

mazestart = (1,0)
mazeend = [3,5]
maze = [[0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]]

if find_maze_path(maze):
    print("I found the maze.")
    print("Path :", mazepath)
else:
    print("I couldn't found the maze.")
