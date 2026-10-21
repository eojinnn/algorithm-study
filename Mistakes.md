# Debugging Notes

Record the mistakes that are likely to recur, not every typo.

| Date | Problem | Mistake | Prevention |
| :--- | :--- | :--- | :--- |
| 2026-10-21 | [Programmers 42586 - 기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586) | Forgot to append the final release group during a later re-solve. | In grouping loops, ask: **Who stores the final group after the loop ends?** |

## Quick Edge-Case Checklist

- Single element
- All elements belong to one group
- New group starts at the final element
- Duplicate values / ties
- Empty input, if permitted by the problem constraints
- Maximum input size and time complexity
