def find_corrupt_pair(nums):
    n = len(nums)
    num_set = set()
    duplicate = -1
    
    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)
        
    actual_sum = sum(nums) - duplicate
    expected_sum = n * (n + 1) // 2
    missing = expected_sum - actual_sum
    
    return [missing, duplicate]
