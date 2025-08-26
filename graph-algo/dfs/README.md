## `algorithms/dfs.md`
```markdown
# Depth-First Search (DFS)
```

## Concept
Depth-First Search explores a graph deeply before backtracking.  
It can be implemented using **recursion** (stack implicitly) or an explicit **stack**.

- Visit the starting node.
- Recursively visit an unvisited neighbor.
- Backtrack when no unvisited neighbors remain.

---

## Example Graph
A
/
B C
| |
D E


Starting from `A` → Order of traversal: `A → B → D → C → E`

---

## Python Code (Recursive)

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }
    dfs_recursive(graph, 'A')
```

# Iterative with Stack
```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))  # Reverse for correct order

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }
    dfs_iterative(graph, 'A')
```
# Applications
- Detecting cycles in graphs
- Topological sorting
- Pathfinding in mazes
- Solving puzzles like Sudoku
