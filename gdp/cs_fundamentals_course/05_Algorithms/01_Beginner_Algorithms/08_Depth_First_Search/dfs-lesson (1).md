# Depth-First Search (DFS)

> An algorithm that dives deep into a graph before backtracking — exploring every path to its end before trying another.

---

## What is DFS?

Depth-First Search traverses a graph by going as far as possible down one branch **before backtracking**. Think of it like exploring a maze: you follow one path until you hit a dead end, then backtrack to the last fork and try another route.

DFS can be implemented with **recursion** (using the call stack implicitly) or an **explicit stack** data structure. Both approaches produce identical behavior.

---

## How it Works

1. **Start at Source** — Pick a starting node and mark it as visited.
2. **Explore Neighbors** — Look at the current node's unvisited neighbors in adjacency list order.
3. **Recurse** — Call DFS on the first unvisited neighbor — go as deep as possible.
4. **Backtrack** — When all neighbors are visited (or none exist), return to the previous node.
5. **Terminate** — Repeat until all reachable nodes have been visited.

---

## Pseudocode (Recursive)

```
procedure DFS(graph, node, visited)
  // Mark this node so we don't revisit it
  mark node as visited

  for each neighbor of node:
    if neighbor is not visited:
      DFS(graph, neighbor, visited)   // recurse deeper
    end if
  end for
  // All neighbors done → backtrack automatically
end procedure
```

---

## Python Implementation

We represent the graph as an **adjacency list** (a dictionary mapping each node to its list of neighbors).

```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()             # initialize on first call

    visited.add(node)               # mark as visited
    print(node, end=" ")

    for neighbor in graph.get(node, []):
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
```

### Visualizing the Graph

```
        A
       / \
      B   C
     / \   \
    D   E   F
         \
          F  ← (already visited via E)
```

### Trace of Execution

| Step | Node | Action | Call Stack |
|------|------|--------|------------|
| 1 | A | Visit, explore B | [A] |
| 2 | B | Visit, explore D | [A, B] |
| 3 | D | Visit, dead end | [A, B, D] |
| 4 | B | Backtrack, explore E | [A, B] |
| 5 | E | Visit, explore F | [A, B, E] |
| 6 | F | Visit, dead end | [A, B, E, F] |
| 7 | A | Backtrack, explore C | [A] |
| 8 | C | Visit, F already visited | [A, C] |
| — | **Done** | **Output: A B D E F C** | [] |

---

## Complexity Analysis

| Case | Time | Space | Notes |
|------|------|-------|-------|
| General | **O(V + E)** | **O(V)** | Visit each vertex once; traverse each edge once. |
| Dense Graph | **O(V²)** | **O(V)** | With adjacency matrix where E ≈ V². |
| Tree (no cycles) | **O(N)** | **O(H)** | H = height; stack depth equals tree height. |

- **V** = number of vertices, **E** = number of edges
- Space is dominated by the recursion stack (or explicit stack), which can hold at most O(V) frames in the worst case (a linear chain graph).

---

## Real-World Applications

- **Maze solving** — DFS follows one path to completion before trying alternatives.
- **Topological sorting** — Used in compilers to resolve build/dependency order.
- **Cycle detection** — Detecting circular imports or dependency loops.
- **Strongly connected components** — Tarjan's and Kosaraju's algorithms.
- **Puzzle solving** — Sudoku, N-Queens, and other backtracking problems.
- **Web crawling** — Following links as deep as possible before backtracking.

---

## Exercises

### Q1 — Trace the Traversal
Trace DFS for the example graph starting from `'A'`. Why might the output differ if the order of neighbors in the adjacency list is different?

<details>
<summary>Answer</summary>

**Trace:** A → B → D (dead end, backtrack) → E → F (dead end, backtrack) → backtrack to A → C → F (already visited).

**Output: `A B D E F C`**

**Why order matters:** DFS explores neighbors in the order they appear in the adjacency list. If `'C'` were listed before `'B'` in A's neighbors, the traversal would go `A → C → F → B → D → E` (F already visited). Same graph topology, different traversal order.

</details>

---

### Q2 — Complexity
What is the time and space complexity of DFS? Justify your answer.

<details>
<summary>Answer</summary>

**Time: O(V + E)** — Each vertex is visited exactly once (O(V)), and for each vertex we examine all its edges (O(E) total across all vertices).

**Space: O(V)** — The visited set is O(V). The recursion stack depth is at most O(V) in the worst case (a linear chain graph A → B → C → … → Z). For iterative DFS with an explicit stack, the stack can also hold up to O(V) elements.

</details>

---

### Q3 — Applications
Name three real-world applications of DFS and explain why DFS (rather than BFS) is a natural fit for each.

<details>
<summary>Answer</summary>

1. **Maze solving** — DFS commits to one path until it's exhausted, which mirrors the intuitive "follow the wall" strategy. BFS would find the *shortest* path, but for simply finding *any* exit, DFS uses less memory.

2. **Topological sorting** — A node's post-order finish time in DFS directly yields a valid topological order (reverse the finish times). This property doesn't arise naturally from BFS.

3. **Cycle detection in directed graphs** — DFS tracks nodes on the *current recursion path* (the "recursion stack"). A back-edge to a node already on this path proves a cycle. BFS doesn't maintain path state in the same way.

</details>

---

### Q4 — Cycle Detection (Challenge)
How would you modify DFS to detect whether a directed graph contains a cycle? What extra data structure do you need?

<details>
<summary>Answer</summary>

Track **two sets**: `visited` (all ever-visited nodes) and `rec_stack` (nodes on the *current* recursion path).

```python
def has_cycle(graph, node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True  # back edge → cycle found

    rec_stack.remove(node)  # leaving this path
    return False


def detect_cycle(graph):
    visited, rec_stack = set(), set()
    return any(
        has_cycle(graph, node, visited, rec_stack)
        for node in graph
        if node not in visited
    )
```

**Key insight:** A node in `visited` but *not* in `rec_stack` was fully explored via another path — safe. A node in `rec_stack` means we've found a back edge → cycle. Time complexity remains O(V + E).

</details>

---

## DFS vs BFS — Quick Comparison

| | DFS | BFS |
|---|---|---|
| **Data structure** | Stack (or recursion) | Queue |
| **Explores** | Deep first | Wide first |
| **Finds shortest path?** | No | Yes (unweighted) |
| **Memory (sparse graph)** | O(V) — stack depth | O(V) — frontier width |
| **Best for** | Topological sort, cycle detection, backtracking | Shortest path, level-order traversal |
