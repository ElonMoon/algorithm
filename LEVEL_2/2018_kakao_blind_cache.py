def solution(cacheSize, cities):
    answer = 0
    lru = []
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.upper()
        if not city in lru:
            if len(lru) < cacheSize:
                lru.append(city)
            else:
                lru.pop(0)
                lru.append(city)
            answer += 5
        else:
            lru.remove(city)
            lru.append(city)
            answer += 1
    return answer
