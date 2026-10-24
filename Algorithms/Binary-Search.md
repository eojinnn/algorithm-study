# Binary Search (이분탐색)

> 탐색 범위를 **절반씩 줄여** 원하는 값이나 조건을 만족하는 경계를 찾는 알고리즘.

## 1. 핵심 개념

- **일반 이분탐색:** 정렬된 배열에서 특정 값을 탐색한다.
- **매개변수 탐색(Parametric Search):** 정답 후보 `mid`가 가능한지 판정하여 **최솟값 / 최댓값**을 찾는다.
- **적용 조건:** 탐색 범위에 **단조성**이 있어야 한다. (예: 불가능 → 가능, 가능 → 불가능)
- **핵심 순서:** `left, right` 설정 → `mid` 계산 → 조건 검사 → 범위 갱신.

## 2. 기본 템플릿: 정렬된 배열에서 값 찾기

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # 찾지 못함
```

## 3. 매개변수 탐색 템플릿

### A. 조건을 만족하는 **최솟값** 찾기

조건이 `False → True` 순서로 바뀔 때 사용한다.

```python
# right는 조건을 만족하는 상한으로 설정
while left < right:
    mid = (left + right) // 2

    if feasible(mid):
        right = mid       # 가능: mid 포함해 왼쪽 탐색
    else:
        left = mid + 1   # 불가능: mid 제외

answer = left
```

### B. 조건을 만족하는 **최댓값** 찾기

조건이 `True → False` 순서로 바뀔 때 사용한다.

```python
# left는 조건을 만족하는 하한으로 설정
while left < right:
    mid = (left + right + 1) // 2  # 올림: 무한 루프 방지

    if feasible(mid):
        left = mid        # 가능: mid 포함해 오른쪽 탐색
    else:
        right = mid - 1  # 불가능: mid 제외

answer = left
```

> 위 두 템플릿은 범위에 정답이 존재하도록 상한/하한을 잡는 방식이다. 정답이 없을 수도 있는 문제라면 별도의 예외 처리 또는 경계 밖의 센티널 값이 필요하다.

## 4. Python 핵심 함수: `bisect`

```python
from bisect import bisect_left, bisect_right

# arr는 오름차순 정렬되어 있어야 함
left_idx = bisect_left(arr, target)    # target 이상이 처음 나타나는 위치
right_idx = bisect_right(arr, target)  # target 초과가 처음 나타나는 위치

count = right_idx - left_idx           # target의 등장 횟수
exists = left_idx < len(arr) and arr[left_idx] == target
```

- `bisect_left`: 같은 값이 있으면 **왼쪽** 삽입 위치.
- `bisect_right`: 같은 값이 있으면 **오른쪽** 삽입 위치.
- `bisect` 함수는 **정렬된 배열**을 전제로 한다.

## 5. 시간복잡도

| 방식 | 시간복잡도 | 추가 공간복잡도 |
| --- | --- | --- |
| 일반 이분탐색 | `O(log N)` | `O(1)` |
| `bisect_left / bisect_right` | `O(log N)` | `O(1)` |
| 매개변수 탐색 | `O(판정 비용 × log R)` | 판정 함수에 따라 다름 |

`R`: 정답 후보 탐색 범위의 크기. 정렬이 필요한 경우 정렬 비용 `O(N log N)`은 별도로 계산한다.

## 6. 실전 체크리스트

1. **정렬 또는 단조성**이 있는가?
2. `mid`는 **무엇의 값**인가? (인덱스, 시간, 길이 등)
3. `feasible(mid)`의 **판정 기준**은 무엇인가?
4. 찾는 것이 **최솟값인지 최댓값인지**에 따라 범위를 올바르게 갱신했는가?
5. `left = mid`처럼 범위가 줄지 않아 **무한 루프**가 생기지 않는가?
6. 탐색 범위에 **정답이 존재하는지** 확인했는가?

---

**암기 포인트:** `mid`로 가능 여부 판정 → **가능/불가능의 경계** 찾기. 최솟값은 `right = mid`, 최댓값은 `left = mid`(단, `mid` 올림) 패턴.
