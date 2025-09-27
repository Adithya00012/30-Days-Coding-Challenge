import math

def minimize_gas_distance(stations: list[int], k: int) -> float:
    low = 0
    high = stations[-1] - stations[0]
    for _ in range(100):
        mid = (low + high) / 2.0
        if mid == 0:
            low = mid
            continue

        if check(stations, k, mid):
            high = mid
        else:
            low = mid
            
    return high

def check(stations: list[int], k: int, max_dist: float) -> bool:
    stations_needed = 0
    for i in range(len(stations) - 1):
        gap = stations[i+1] - stations[i]
        if gap > max_dist:
            stations_needed += math.ceil(gap / max_dist) - 1
            
    return stations_needed <= k
