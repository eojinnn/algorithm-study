# Sorting in Python

Python에서 자주 사용하는 정렬 방법과 `key` 인자를 정리한 노트입니다.

## 1. `sort()` vs `sorted()`

```python
nums = [3, 1, 4, 2]

nums.sort()              # 원본 리스트를 직접 변경
print(nums)              # [1, 2, 3, 4]

nums = [3, 1, 4, 2]
result = sorted(nums)     # 새로운 리스트를 반환
print(result)            # [1, 2, 3, 4]
print(nums)              # [3, 1, 4, 2] (원본 유지)
```

| 방법 | 원본 변경 | 반환값 | 사용 예시 |
| --- | --- | --- | --- |
| `arr.sort()` | O | `None` | 이미 가진 리스트를 정렬할 때 |
| `sorted(arr)` | X | 정렬된 새 리스트 | 원본을 보존하거나 다른 iterable을 정렬할 때 |

> **주의:** `result = arr.sort()`는 `result`에 `None`을 저장합니다.

## 2. 오름차순과 내림차순

```python
arr = [4, 1, 3, 2]

print(sorted(arr))                # [1, 2, 3, 4]
print(sorted(arr, reverse=True))  # [4, 3, 2, 1]
```

- 기본값: 오름차순 (`reverse=False`)
- `reverse=True`: 정렬 순서를 뒤집음

## 3. `key`로 정렬 기준 지정하기

`key`에는 **각 원소를 어떤 값으로 비교할지 정하는 함수**를 전달합니다.

```python
words = ["pear", "a", "banana", "kiwi"]

print(sorted(words, key=len))
# ['a', 'pear', 'kiwi', 'banana']

nums = [-10, 3, -2, 7]
print(sorted(nums, key=abs))
# [-2, 3, 7, -10]
```

### `lambda` 기본 형태

```python
sorted(data, key=lambda x: x[1])
```

- `x`: 정렬 대상의 원소 하나
- `x[1]`: 원소를 비교할 때 사용할 기준 값 (두 번째 항목)
- `lambda x: ...`: 간단한 익명 함수

## 4. 2차원 리스트 정렬

```python
arr = [[1, 4], [3, 2], [2, 5]]

# 첫 번째 값 기준 오름차순
print(sorted(arr, key=lambda x: x[0]))
# [[1, 4], [2, 5], [3, 2]]

# 두 번째 값 기준 오름차순
print(sorted(arr, key=lambda x: x[1]))
# [[3, 2], [1, 4], [2, 5]]

# 두 번째 값 기준 내림차순
print(sorted(arr, key=lambda x: x[1], reverse=True))
# [[2, 5], [1, 4], [3, 2]]
```

## 5. 여러 조건으로 정렬 (중요)

```python
scores = [("kim", 90), ("lee", 80), ("park", 90), ("choi", 80)]

# 1순위: 점수 내림차순, 2순위: 이름 오름차순
result = sorted(scores, key=lambda x: (-x[1], x[0]))
print(result)
# [('kim', 90), ('park', 90), ('choi', 80), ('lee', 80)]
```

**원리:** `key`가 튜플을 반환하면 앞 요소부터 비교하고, 값이 같을 때 다음 요소를 비교합니다.

- `x[1]`: 점수 오름차순
- `-x[1]`: 점수 내림차순 (**숫자일 때**)
- `x[0]`: 이름 오름차순

```python
points = [[2, 3], [1, 3], [3, 1], [4, 1]]

# 두 번째 값 오름차순 -> 첫 번째 값 내림차순
print(sorted(points, key=lambda x: (x[1], -x[0])))
# [[4, 1], [3, 1], [2, 3], [1, 3]]
```

> `reverse=True`를 쓰면 정렬 기준 **전체가 뒤집힙니다.** 한 기준만 내림차순으로 만들고 싶을 때는 숫자에 `-`를 붙이는 방법이 편리합니다.

## 6. 딕셔너리 리스트 정렬

```python
students = [
    {"name": "kim", "score": 90},
    {"name": "lee", "score": 80},
    {"name": "park", "score": 90},
]

# 점수 내림차순, 이름 오름차순
result = sorted(students, key=lambda x: (-x["score"], x["name"]))
print([s["name"] for s in result])  # ['kim', 'park', 'lee']
```

## 7. 문자열 정렬

```python
words = ["Banana", "apple", "Cherry"]

print(sorted(words))                  # ['Banana', 'Cherry', 'apple']
print(sorted(words, key=str.lower))   # ['apple', 'Banana', 'Cherry']
```

- 기본 문자열 정렬은 대소문자를 구별합니다.
- 대소문자 무시: `key=str.lower` 또는 `key=str.casefold`
- 숫자가 문자열이면 수의 크기가 아닌 문자열 순서로 정렬됩니다. 필요하다면 `key=int`를 사용합니다.

## 8. 정렬 안정성 (Stable Sort)

Python의 `sort()`와 `sorted()`는 **안정 정렬**입니다. `key` 값이 같은 원소는 기존 상대적 순서를 유지합니다.

```python
items = [("A", 10), ("B", 5), ("C", 10)]
print(sorted(items, key=lambda x: x[1]))
# [('B', 5), ('A', 10), ('C', 10)]
```

## 9. 시간복잡도

| 연산 | 일반적인 시간복잡도 |
| --- | --- |
| `arr.sort()` | O(N log N) 최악, 이미 정렬된 경우 O(N) 가능 |
| `sorted(arr)` | O(N log N) 최악, 이미 정렬된 경우 O(N) 가능 |

Python은 Timsort 기반 정렬을 사용합니다. `key=lambda x: ...`에서 key 계산 자체가 매우 비싸다면 그 비용도 고려해야 합니다.

## 10. 코딩테스트 직전 치트시트

```python
arr.sort()                                     # 원본 오름차순
arr.sort(reverse=True)                        # 원본 내림차순
b = sorted(arr)                               # 새 리스트 오름차순
b = sorted(arr, key=lambda x: x[1])           # 두 번째 값 오름차순
b = sorted(arr, key=lambda x: -x[1])          # 두 번째 숫자값 내림차순
b = sorted(arr, key=lambda x: (x[0], x[1]))   # 1순위 첫 번째, 2순위 두 번째
b = sorted(arr, key=lambda x: (-x[1], x[0]))  # 두 번째 숫자값 ↓, 첫 번째 값 ↑
```

### 자주 하는 실수

1. `arr.sort()`의 반환값을 리스트로 착각하기 (`None` 반환)
2. `reverse=True`가 특정 조건만이 아니라 **모든 조건**을 뒤집는다는 점을 잊기
3. `x[0]`, `x[1]`를 잘못 선택하기
4. 정렬 후 기존 원소 순서를 보존해야 하는 문제에서 원본 리스트를 수정하기

## Related Problems

- [프로그래머스 - K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748)
- [프로그래머스 - 가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746)
- [프로그래머스 - H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747)
