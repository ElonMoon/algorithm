def solution(brown, yellow):
    for i in range(1, int(yellow ** .5)+1):
        if not yellow % i:
            if 2*(i + yellow//i)+4 == brown:
                return [yellow//i+2, i+2]
