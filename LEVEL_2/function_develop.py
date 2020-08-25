import math


def solution(progresses, speeds):
    answer = []
    work_list = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    pivot = 0
    count = 1
    for idx in range(1, len(work_list)):
        if work_list[pivot] < work_list[idx]:
            answer.append(count)
            count = 1
            pivot = idx
        else:
            count += 1
    answer.append(count)
    return answer
