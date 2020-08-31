def solution(n):
    answer = ''
    strange = ['4', '1', '2']
    while n:
        n, mod = divmod(n, 3)
        answer = strange[mod] + answer
        if mod == 0:
            n -= 1
    return answer
