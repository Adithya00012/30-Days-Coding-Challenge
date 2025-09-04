import heapq

def kth_smallest_prime_fraction(arr, k):
    n = len(arr)
    min_heap = []
    for i in range(n - 1):
        heapq.heappush(min_heap, (arr[i] / arr[n-1], i, n - 1))
    for _ in range(k - 1):
        _, i, j = heapq.heappop(min_heap)
        if j > i + 1:
            next_j = j - 1
            heapq.heappush(min_heap, (arr[i] / arr[next_j], i, next_j))
    _, i, j = min_heap[0]
    return [arr[i], arr[j]]

