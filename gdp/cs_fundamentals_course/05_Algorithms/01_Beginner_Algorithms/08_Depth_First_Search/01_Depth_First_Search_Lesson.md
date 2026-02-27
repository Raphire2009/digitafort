# Depth-First Search (DFS) Lesson

Depth-First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

DFS is commonly implemented using recursion (which uses the call stack) or an explicit stack.

## How it Works

1.  **Start at the source:** Pick a starting node and mark it as visited.
2.  **Explore neighbor:** Look at the neighbors of the current node.
3.  **Recursive Step:** If a neighbor has not been visited, recursively call DFS on that neighbor.
4.  **Backtrack:** If all neighbors of the current node have been visited (or it has no neighbors), go back to the previous node (backtrack).
5.  **Repeat:** Continue until all reachable nodes have been visited.

## Pseudocode (Recursive)

```
procedure DFS(graph, node, visited)
  mark node as visited
  for each neighbor of node
    if neighbor is not visited
      DFS(graph, neighbor, visited)
    end if
  end for
end procedure
```

## Python Implementation

We use an adjacency list to represent the graph.

```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current node as visited
    visited.add(node)
    print(node, end=" ")

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage (Adjacency List):
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal starting from 'A':")
dfs(graph, 'A')
# Expected Output: A B D E F C 
```

## Exercise

1.  Trace DFS for the example graph starting from 'A'. Why might the output differ if the order of neighbors in the adjacency list is different?
2.  What is the time and space complexity of DFS?
3.  Name one real-world application of DFS (e.g., solving a maze).
