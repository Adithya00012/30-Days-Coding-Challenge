from union_find import UnionFind
import heapq

def get_skyline(buildings):
    if not buildings:
        return []
    events = []
    for left, right, height in buildings:
        events.append((left, -height))  
        events.append((right, height))   
    events.sort()
    max_heights = [0]
    result = []
    current_max_height = 0

    for x, height in events:
        prev_max_height = -max_heights[0]
        if height < 0:
            heapq.heappush(max_heights, height)
        else:
            max_heights.remove(-height)
            heapq.heapify(max_heights)
        current_max_height = -max_heights[0]
        if prev_max_height != current_max_height:
            if result and result[-1][0] == x:
                result[-1][1] = current_max_height
            else:
                result.append([x, current_max_height])
    return result
