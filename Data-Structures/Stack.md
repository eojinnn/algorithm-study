# Stack

A **stack** follows **LIFO (Last In, First Out)**: the most recently added item is removed first.

## Python Implementation

Use a built-in `list` as a stack.

```python
stack = []
stack.append(10)   # push
stack.append(20)
print(stack[-1])   # peek -> 20
print(stack.pop()) # pop  -> 20
print(len(stack))  # size -> 1
if stack:
    print("not empty")
```

## Common Operations

| Operation | Python | Time complexity |
| :--- | :--- | :--- |
| Push | `stack.append(x)` | O(1) amortized |
| Pop | `stack.pop()` | O(1) |
| Peek | `stack[-1]` | O(1) |
| Size | `len(stack)` | O(1) |
| Is not empty | `bool(stack)` | O(1) |

**Caution:** `pop()` and `stack[-1]` raise an exception on an empty stack.

## Typical Pattern: Matching Parentheses

```python
def is_valid_parentheses(s):
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                return False
            stack.pop()
    return not stack
```

## When to Use

- Parenthesis matching and expression evaluation
- Undo operations and backtracking
- Iterative DFS
- Monotonic stack patterns
