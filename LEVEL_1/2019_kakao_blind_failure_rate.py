def solution(N, stages):
    d = []
    players = len(stages)
    a = []
    for i in range(1, N+2):
        d.append(stages.count(i))
    for i in range(N):
        fail = sum(d[:i])
        a.append(d[i]/(players-fail) if players-fail != 0 else 0)
    b = [(idx, value) for idx, value in enumerate(a)]
    c = sorted(b, key=lambda x: x[1], reverse=True)
    return [key+1 for key, value in c]
