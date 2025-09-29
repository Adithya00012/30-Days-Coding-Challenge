def two_single_numbers(nums):
    bitwise_xor = 0
    for num in nums:
        bitwise_xor ^= num

    bitwise_mask = bitwise_xor & -bitwise_xor

    result = 0
    
    for num in nums:
        if num & bitwise_mask:
            result ^= num
    
    return [result, bitwise_xor ^ result]
