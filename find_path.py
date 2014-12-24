def find_path(graph, start, end, path=[]):

    if start not in graph: return None

    path += [start]

    # Path found. Base case
    if start == end: return path

    for node in graph[start]:
        if node not in path:
            # Recursively search path
            return find_path(graph, node, end, path)

    return None

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']
        }

print find_path(graph, 'A', 'C')
