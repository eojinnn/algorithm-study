# Queue and Deque

A **queue** follows **FIFO (First In, First Out)**: the earliest item added is removed first.

In Python, prefer `collections.deque` over a `list` when removing items from the front.

## Python Implementation

```python
from collections import deque

q = deque()
q.append(10)         # enqueue to the right
q.append(20)
print(q[0])          # front -> 10
print(q.popleft())   # dequeue -> 10
print(q[-1])         # rear -> 20
print(len(q))        # size -> 1
```

## Common Operations

| Operation | Python | Time complexity |
| :--- | :--- | :--- |
| Add to rear | `q.append(x)` | O(1) |
| Remove from front | `q.popleft()` | O(1) |
| Add to front | `q.appendleft(x)` | O(1) |
| Remove from rear | `q.pop()` | O(1) |
| Inspect front/rear | `q[0]`, `q[-1]` | O(1) |
| Size | `len(q)` | O(1) |

**Caution:** `q.popleft()` raises `IndexError` if the queue is empty.

### Rotation

```python
from collections import deque
q = deque([1, 2, 3])
q.rotate(1)   # deque([3, 1, 2])
q.rotate(-1)  # deque([1, 2, 3])
```

### Why Not `list.pop(0)`?

```python
items = [1, 2, 3]
items.pop(0)  # O(N): remaining items must shift
```

Repeated removals from the front are more efficient with `deque.popleft()` (O(1)). Note that arbitrary middle indexing is not O(1) for a deque.

## Typical Pattern: BFS

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

## When to Use

- BFS and unweighted shortest path
- Processing tasks in arrival order
- Simulations with enqueue and dequeue
