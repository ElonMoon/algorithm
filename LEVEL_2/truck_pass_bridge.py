def solution(bridge_length, weight, truck_weights):
    bridge = [] * bridge_length
    answer = 0
    while bridge_length > 0:
        if len(truck_weights) == 0:
            continue
        if len(bridge) < bridge_length:
            if sum(bridge) < weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.pop(0)
                bridge.append(truck_weights.pop(0))
        else:
            bridge.pop(0)
        answer += 1
        bridge_length -= 1
    return answer
