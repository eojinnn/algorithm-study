# Brute Force & Backtracking

> 가능한 경우를 탐색하는 알고리즘. **완전탐색은 탐색 범위**, **백트래킹은 선택과 복구를 이용한 탐색 방식**이다.

## 1. 완전탐색 (Brute Force)

- **개념:** 가능한 후보를 확인해 조건을 만족하는 답이나 최적값을 찾는다.
- **기본 방식:** 반복문, 순열/조합, 비트마스크, DFS 등.
- **사용 판단:** 입력이 작아 모든 후보를 검사할 수 있는지 먼저 계산한다.

### Python 핵심 함수 (`itertools`)

```python
from itertools import permutations, combinations, product, combinations_with_replacement

arr = [1, 2, 3]

permutations(arr)                  # 전체 순열: 순서 O, 중복 선택 X
permutations(arr, 2)               # 2개 순열
combinations(arr, 2)               # 2개 조합: 순서 X, 중복 선택 X
product(arr, repeat=2)             # 2개 선택: 순서 O, 중복 선택 O
combinations_with_replacement(arr, 2)  # 2개 선택: 순서 X, 중복 선택 O

for order in permutations(arr):    # 결과를 하나씩 꺼내기 (tuple)
    pass
```

| 필요한 경우 | 선택 |
| --- | --- |
| **순서가 중요**하고 재사용 불가 | `permutations()` |
| 순서가 무관하고 재사용 불가 | `combinations()` |
| 순서가 중요하고 재사용 가능 | `product(..., repeat=r)` |
| 순서가 무관하고 재사용 가능 | `combinations_with_replacement()` |
| 각 원소를 선택/미선택 | 비트마스크 또는 DFS |

> `list(permutations(arr))`는 모든 결과를 메모리에 저장한다. 순회만 필요하면 `for ... in permutations(arr)` 사용.

## 2. 백트래킹 (Backtracking)

- **개념:** 하나를 **선택 → 재귀 탐색 → 선택 취소(복구)** 하며 다른 경우도 확인한다.
- **핵심:** `visited`, 현재 상태(`path`, 남은 자원 등), **종료 조건**, **가지치기**.
- **DFS와 관계:** DFS로 구현하는 경우가 많지만, 모든 DFS에서 상태 복구가 필요한 것은 아니다.

### 기본 템플릿: 중복 없이 r개를 순서 있게 선택

```python
def solve(arr, r):
    visited = [False] * len(arr)
    path = []
    result = []

    def dfs():
        if len(path) == r:           # 종료 조건
            result.append(path[:])  # 복사해서 저장
            return

        for i in range(len(arr)):
            if visited[i]:
                continue
            # if 선택 불가능한 조건: continue  # 가지치기

            visited[i] = True       # 1. 선택
            path.append(arr[i])
            dfs()                   # 2. 재귀 탐색
            path.pop()             # 3. 선택 취소
            visited[i] = False

    dfs()
    return result
```

### 실전 체크리스트

1. **상태 정의:** `dfs(...)`가 무엇을 뜻하는가?
2. **종료 조건:** 언제 정답을 기록하고 `return`하는가?
3. **후보 탐색:** 무엇을 선택할 수 있는가?
4. **가지치기:** 불가능한 경우를 미리 건너뛸 수 있는가?
5. **상태 복구:** 재귀 호출 후 `path.pop()`, `visited[i] = False` 등을 빠뜨리지 않았는가?

## 3. 시간복잡도 빠른 판단

| 탐색 방식 | 경우의 수 (상한) |
| --- | --- |
| N개 전체 순열 | `N!` |
| N개 중 r개 순열 | `N! / (N-r)!` |
| N개 중 r개 조합 | `N! / (r!(N-r)!)` |
| N개 원소의 부분집합 | `2^N` |
| N개 후보에서 r번 중복 선택 | `N^r` |

실제 **시간복잡도 = 탐색 후보 수 × 후보당 검사 비용**. 백트래킹은 가지치기로 실제 탐색 수를 줄일 수 있지만, 최악의 경우에는 여전히 지수 또는 팩토리얼 시간이 걸릴 수 있다.

---

**암기 포인트:** 작은 입력 + 모든 순서 확인 → `permutations()` / 상태와 제약이 복잡함 → `DFS + visited + 선택·재귀·복구`.
