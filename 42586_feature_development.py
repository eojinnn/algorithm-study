"""Programmers 42586 - 기능개발.

Original approach: calculate completion days, then group consecutive releases.
Time: O(N).
Note: this version modifies the input list `progresses` in place.
"""

import math


def solution(progresses, speeds):
    for i in range(len(progresses)):
        progresses[i] = 100 - progresses[i]
        progresses[i] = math.ceil(progresses[i] / speeds[i])

    maximum = progresses[0]
    release = 0
    ans = []
    for i in range(len(progresses)):
        if progresses[i] <= maximum:
            release += 1
            continue
        ans.append(release)
        maximum = progresses[i]
        release = 1
    ans.append(release)
    return ans
