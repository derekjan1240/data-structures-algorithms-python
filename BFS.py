graph = {'A': set(['B', 'D']),
         'B': set(['C', 'E']),
         'C': set(['E', 'F']),
         'D': set(['G']),
         'E': set(['D', 'F', 'G', 'H']),
         'F': set(['H']),
         'G': set({'H'}),
         'H': set({})}

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

print(bfs(graph, 'A'))