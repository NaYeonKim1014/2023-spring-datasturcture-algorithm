def dfs(adj_matrix, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for i in range(len(adj_matrix)):
        if adj_matrix[start][i] == 1 and i not in visited:
            dfs(adj_matrix, i, visited)

adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 1, 0],
]

dfs(adj_matrix, 0) # start from vertex 0

