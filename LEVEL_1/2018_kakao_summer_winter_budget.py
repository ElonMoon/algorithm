def solution(d, budget):
    answer = 0
    sorted_d = sorted(d)
    for idx, req in enumerate(sorted_d):
        k = sum(sorted_d[:idx+1])
        if k <= budget:
            answer += 1
    return answer
