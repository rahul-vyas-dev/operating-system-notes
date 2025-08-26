# Dijkstra’s Shortest Path Algorithm

## Concept
Dijkstra’s algorithm finds the shortest path in a weighted graph with non-negative edge weights.

### Key Idea
- Maintain a distance table.
- Pick the unvisited node with the smallest tentative distance.
- Update neighbor distances.
- Repeat until all nodes are visited.

## Example Graph
A --2--> B --1--> C
|
4 5
↓
D-----------E

From `A` to all nodes:
- A → B: 2  
- A → D: 4  
- A → C via B: 3  
- A → E via B → C → E: 8

## Python Code

```python
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, node = heapq.heappop(heap)
        if current_dist > dist[node]:
            continue
        for neighbor, weight in graph[node].items():
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist

if __name__ == "__main__":
    graph = {
        'A': {'B': 2, 'D': 4},
        'B': {'C': 1, 'E': 5},
        'C': {'E': 3},
        'D': {'E': 1},
        'E': {}
    }
    print(dijkstra(graph, 'A'))
