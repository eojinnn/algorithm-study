# 42586. 기능개발

- **Platform:** [Programmers](https://school.programmers.co.kr/learn/courses/30/lessons/42586)
- **Category:** Ordered grouping (listed as Stack / Queue on Programmers)
- **Language:** Python
- **Time complexity:** O(N)
- **Solution:** [42586_feature_development.py](42586_feature_development.py)

## Idea

1. Calculate the number of days required for each task to finish.
2. Maintain the release day determined by the earliest task in the current group.
3. If the next task finishes by that day, include it in the same release.
4. Otherwise, save the group count and start a new group.
5. After the loop, **append the last group**.

## Complexity

- **Time:** O(N) - one pass to compute completion days and one pass to group releases.
- **Auxiliary space:** O(1) apart from the answer list, because the original `progresses` list is modified in place.

## Review

- The queue-like ordering rule does not require an explicit `deque` here.
- **Mistake to avoid:** failing to append the final group after the loop.
- **Possible refinement:** preserve the input list and use integer ceiling division instead of `math.ceil`.
