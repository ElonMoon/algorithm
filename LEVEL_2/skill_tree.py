"""
Summer/Winter Coding
"""


def solution(skill: str, skill_trees: list) -> int:
    answer = 0
    for tree in skill_trees:
        s = list(skill)
        chk = True
        for val in tree:
            if val in s and s.index(val) == 0:
                s.remove(val)
            elif val in s and s.index(val) != 0:
                chk = False
                break
        if chk:
            answer += 1
    return answer
