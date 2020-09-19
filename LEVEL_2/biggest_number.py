def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda n: n*3, reverse=True)
    answer = str(int(''.join(list(map(str, numbers)))))
    return answer
