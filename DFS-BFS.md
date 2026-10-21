# DFS and BFS

Two basic graph traversal strategies.

| | DFS | BFS |
| :--- | :--- | :--- |
| Exploration | Go deep first | Visit level by level |
| Data structure | Stack / recursion | Queue (`deque`) |
| Common use | Reachability, exhaustive search | Minimum edges in an unweighted graph |

## DFS (Iterative Stack)

```python
def dfs(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for nxt in graph[node]:
            if nxt not in visited:
                stack.append(nxt)
    return visited
```

## BFS (Queue)

```python
from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = {start}
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return visited
```

## Complexity

For an adjacency-list graph, traversal is **O(V + E)** time and **O(V)** auxiliary space in the usual implementation, where V is the number of vertices and E is the number of edges.

## Common Mistakes

- Forgetting to mark a node as visited, causing repeated work or cycles.
- Confusing DFS traversal with the shortest path guarantee of BFS in unweighted graphs.
- In grid BFS, forgetting bounds checks and obstacle checks.
- Using `list.pop(0)` instead of `deque.popleft()` for large queues.
