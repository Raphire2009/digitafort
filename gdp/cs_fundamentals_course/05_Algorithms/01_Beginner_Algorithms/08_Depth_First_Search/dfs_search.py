def dfs_search(graph, node, target, visited=None):
    if visited is None:
        visited = set()

    if node in visited:
        return False

    visited.add(node)

    if node == target:
        return True

    for neighbor in graph.get(node, []):
        if dfs_search(graph, neighbor, target, visited):
            return True

    return False


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

print("Search E from A:", dfs_search(graph, "A", "E"))  # True
print("Search Z from A:", dfs_search(graph, "A", "Z"))  # False
