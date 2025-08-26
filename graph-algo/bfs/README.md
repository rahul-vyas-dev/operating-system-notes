# Breadth-First Search (BFS)

## Concept
Breadth-First Search explores a graph level by level (like ripples spreading out from a stone dropped in water).  
It is implemented using a **queue**.

- Visit the starting node.
- Add all its unvisited neighbors to the queue.
- Dequeue nodes one by one, exploring their neighbors.
- Continue until the queue is empty.

---

## Example Graph

A
/
B C
| |
D E


Starting from `A` → Order of traversal: `A → B → C → D → E`

---

## Python Code

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node] - visited)

if __name__ == "__main__":
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D'},
        'C': {'A', 'E'},
        'D': {'B'},
        'E': {'C'}
    }
    bfs(graph, 'A')
```

# application

- Finding shortest path in unweighted graphs

- Web crawling

- Network broadcasting

- Social network connection suggestions

