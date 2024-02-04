from collections import deque

# define a graph as a dictionary of lists
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start):
    # create a queue for BFS
    queue = deque([start])

    # create a set to keep track of visited nodes
    visited = set([start])

    while queue:
        # get the next node from the queue
        node = queue.popleft()
        print(node, end=' ')

        # add all unvisited neighbors of the current node to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# test the bfs function with node 'A'
bfs('A')
