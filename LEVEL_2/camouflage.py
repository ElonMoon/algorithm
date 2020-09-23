from collections import Counter


def solution(clothes):
    category = Counter([c for _, c in clothes])
    combination = 1
    for key in category:
        combination *= (category[key] + 1)
    return combination - 1
