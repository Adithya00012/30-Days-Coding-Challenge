import heapq

def nth_super_ugly_number(n, primes):
    min_heap = [(p, p, 0) for p in primes]
    ugly_numbers = [1]
    
    while len(ugly_numbers) < n:
        next_ugly, prime, index = heapq.heappop(min_heap)
        if next_ugly != ugly_numbers[-1]:
            ugly_numbers.append(next_ugly)
        heapq.heappush(min_heap, (prime * ugly_numbers[index + 1], prime, index + 1))
        
    return ugly_numbers[-1]
