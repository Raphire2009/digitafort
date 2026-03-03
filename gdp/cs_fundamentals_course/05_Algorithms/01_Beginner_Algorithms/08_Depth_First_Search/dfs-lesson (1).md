# Depth-First Search (DFS)

> An algorithm that dives deep into a graph before backtracking — exploring every path to its end before trying another.

---

## What is DFS?

Depth-First Search traverses a graph by going as far as possible down one branch **before backtracking**. Think of it like exploring a maze: you follow one path until you hit a dead end, then backtrack to the last fork and try another route.

DFS can be implemented with **recursion** (using the call stack implicitly) or an **explicit stack** data structure. Both approaches produce identical behavior.

Two core ideas make DFS work:
- **Go deep first**: At each step, pick one unvisited neighbor and keep moving forward.
- **Never repeat work**: Keep track of visited nodes so you do not loop forever in cyclic graphs.

In short, DFS is a "depth-first + memory" strategy.

---

## How it Works

1. **Start at Source** — Pick a starting node and mark it as visited.
2. **Explore Neighbors** — Look at the current node's unvisited neighbors in adjacency list order.
3. **Recurse** — Call DFS on the first unvisited neighbor — go as deep as possible.
4. **Backtrack** — When all neighbors are visited (or none exist), return to the previous node.
5. **Terminate** — Repeat until all reachable nodes have been visited.

Important note: DFS does **not** guarantee the shortest path. It guarantees a systematic traversal of all reachable nodes.

### Student Mental Model

If DFS were a person exploring tunnels, the behavior would be:
1. Pick one tunnel and keep walking until you cannot continue.
2. Step backward to the last junction with an untried tunnel.
3. Repeat until every reachable tunnel has been tried.

This is exactly why recursion works well: each recursive call represents "go one level deeper."

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

Why this code is written this way:
- `visited=None` then `visited = set()` prevents sharing one set across unrelated DFS runs.
- `graph.get(node, [])` safely handles nodes that are missing from the dictionary.
- `if neighbor not in visited` prevents infinite recursion on cycles like `A -> B -> A`.

### What Happens If We Remove `visited`?

In a graph with a cycle, DFS can run forever:

`A -> B -> C -> A -> B -> C -> ...`

So `visited` is not optional for general graphs.  
In trees (which have no cycles), `visited` is often unnecessary, but keeping it is still a safe, consistent habit for beginners.

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

How to read this table:
- The **Node** column is the node currently being processed.
- The **Call Stack** shows active recursive calls. Deeper recursion means a longer stack.
- When a dead end is reached, the stack shrinks. That shrink is exactly what "backtracking" means.

---

## Complexity Analysis

| Case | Time | Space | Notes |
|------|------|-------|-------|
| General | **O(V + E)** | **O(V)** | Visit each vertex once; traverse each edge once. |
| Dense Graph | **O(V²)** | **O(V)** | With adjacency matrix where E ≈ V². |
| Tree (no cycles) | **O(N)** | **O(H)** | H = height; stack depth equals tree height. |

- **V** = number of vertices, **E** = number of edges
- Space is dominated by the recursion stack (or explicit stack), which can hold at most O(V) frames in the worst case (a linear chain graph).

Intuition:
- You cannot visit more than `V` nodes, so node-work is O(V).
- Across all nodes, you inspect each edge a constant number of times, giving O(E).
- Add them together: **O(V + E)**.

### Time Complexity, Step by Step

When students see `O(V + E)`, a common confusion is:  
"Why not `O(V * E)`?"

It is **not** multiplication because DFS is not doing "every vertex times every edge."  
Instead, it does two kinds of work once across the whole run:

1. **Vertex work** (visit/mark each node) -> up to `V` times
2. **Edge work** (check neighbor connections) -> up to `E` total checks (constant-factor differences by representation)

So total work is an addition:

`Total = vertex work + edge work = O(V) + O(E) = O(V + E)`

### Mini Example

Suppose:
- `V = 6` nodes
- `E = 6` edges

Then DFS does roughly:
- up to 6 node visits
- plus neighbor checks across about 6 edges

So the growth is around `6 + 6`, not `6 * 6`.

### Directed vs Undirected (Quick Note)

- **Directed graph**: each directed edge is considered once in adjacency-list scanning.
- **Undirected graph**: each undirected edge appears in two adjacency lists, so it may be scanned twice (still linear, still O(V + E)).

Big-O ignores constant factors like "once vs twice," so complexity stays the same class.

### Why DFS Space Can Be Large

DFS stores:
- The `visited` set (up to all nodes).
- The active recursion path (or explicit stack).

If the graph is shaped like a long chain, recursion depth can become very large (close to `V`).  
That is the worst-case reason space is O(V).

In Python specifically, very deep recursion may hit the recursion limit. In those cases, iterative DFS with an explicit stack is safer.

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

Rule of thumb for students:
- Use **DFS** when you care about exploring structure deeply (components, cycles, ordering, backtracking).
- Use **BFS** when you care about minimum number of edges from a start node.

---

## Iterative DFS (Stack Version)

Recursive DFS is elegant, but iterative DFS avoids recursion-depth issues.

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()  # LIFO -> depth-first behavior
        if node in visited:
            continue

        visited.add(node)
        print(node, end=" ")

        # Reverse to mimic recursive left-to-right traversal order
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)
```

### Recursive vs Iterative in Practice

- **Recursive DFS**: shorter and easier to read when first learning.
- **Iterative DFS**: more robust for very deep graphs in production code.
- Both have the same big-O complexity.

---

## Disconnected Graphs

Starting DFS from one node only visits nodes reachable from that start node.

To traverse an entire graph with multiple disconnected components:

```python
def dfs_full(graph):
    visited = set()

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)  # reuse recursive DFS
```

This pattern ensures every component is explored.

---

## Common Beginner Mistakes

1. Forgetting to mark nodes as visited before exploring neighbors.
2. Assuming DFS always gives a shortest path.
3. Confusing traversal order with graph structure (order depends on neighbor list order).
4. Thinking recursion "remembers everything" automatically without a visited structure.
5. Testing only acyclic graphs, then failing on cyclic inputs.

---

## Quick Recap

- DFS explores one path deeply, then backtracks.
- `visited` prevents repeated work and infinite loops.
- Complexity is usually **O(V + E)** time and **O(V)** space.
- Neighbor order changes traversal order, but not correctness.
