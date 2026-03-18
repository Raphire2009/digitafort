grid = [
    ["1","1","0","0","0","1","1","0","0","0"],
    ["1","1","0","0","0","1","1","0","0","0"],
    ["0","0","1","0","0","0","0","1","1","0"],
    ["0","0","0","1","1","0","0","1","1","0"],
    ["1","0","0","0","1","0","0","0","0","1"],
    ["1","0","0","0","1","0","1","1","0","0"],
    ["0","0","1","1","0","0","1","1","0","0"],
    ["0","0","1","1","0","0","0","0","1","1"],
    ["1","1","0","0","0","1","0","0","1","1"],
    ["1","1","0","0","0","1","0","0","0","0"],
]

from collections import deque

def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))
        while queue:
            row, col = queue.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and grid[nr][nc] == '1'
                        and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands

print(num_islands(grid))