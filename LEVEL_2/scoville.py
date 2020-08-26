import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while K > scoville[0]:
        if len(scoville) < 2:
            answer = -1
            break
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville) * 2
        s = s1 + s2
        heapq.heappush(scoville, s)
        answer += 1
    return answer
