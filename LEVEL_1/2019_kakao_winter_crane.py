"""
2019 카카오 개발자 겨울 인턴십 크레인 인형뽑기
"""


def solution(board: list, moves: list) -> int:
    answer = 0
    s = []

    for dy in moves:
        for dx in range(len(board)):
            if board[dx][dy - 1] == 0:
                continue
            else:
                s.append(board[dx][dy - 1])
                board[dx][dy - 1] = 0
                break
        if len(s) <= 1:
            continue
        else:
            k = s.pop()
            if s[-1] == k:
                s.pop()
                answer += 2
            else:
                s.append(k)
    return answer
