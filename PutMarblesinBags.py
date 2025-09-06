def put_marbles(weights, k):
    n = len(weights)
    if k == 1 or n == k:
        return 0
    cut_costs = []
    for i in range(1, n):
        cut_costs.append(weights[i-1] + weights[i])
    cut_costs.sort()
    min_score_sum = sum(cut_costs[:k-1])
    max_score_sum = sum(cut_costs[n - k:])
    
    return max_score_sum - min_score_sum

