""" a.k.a Depth first search
"""
# Recursive
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

# Non recursive
def depth_first(graph, start, end):

    stack = [start]
    path = [start]

    while stack:
        node = stack.pop()

        if node == end: return path

        for vertex in graph[node]:
            if vertex not in path:
                path.append(vertex)
                stack.append(vertex)

    return None

# All possible paths from start to end
def all_paths(graph, start, end, path=[]):

    # Creates a new list so input path is not affected
    path = path + [start]

    if start not in graph: return None

    if start == end: return [path]
    paths = []

    for node in graph[start]:

        if node not in path:
            new_paths = all_paths(graph, node, end, path)

            for newpath in new_paths:
                paths.append(newpath)

    return paths

def shortest_path(graph, start, end, path=[]):

    path = path + [start]

    if start not in graph: return None

    if start == end: return path

    shortest = []

    for node in graph[start]:

        if node not in path:
            new_path = shortest_path(graph, node, end, path)

            if not shortest or len(new_path) < len(shortest):
                shortest = new_path

    return shortest

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']
        }

print depth_first(graph, 'A', 'D')
print find_path(graph, 'A', 'D')
print all_paths(graph, 'A', 'D')
print shortest_path(graph, 'A', 'D')
