

"""
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()             # initialize on first call

    visited.add(node)               # mark as visited
    print(node, end=" ")

    for neighbor in graph.get(node, []):
        print(neighbor)
        print()
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# --- Example graph (adjacency list) ---
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')
# Output: A B D E F C
"""



graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : [],
}

def dfs(graph, node , visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)
    print()

    for n in graph.get(node,[]):
        if n not in visited:
            dfs(graph, n, visited)




dfs(graph,"A")