def add_binary(str1, str2):
    res = ""
    i, j = len(str1) - 1, len(str2) - 1
    carry = 0
    
    while i >= 0 or j >= 0 or carry:
        digit1 = int(str1[i]) if i >= 0 else 0
        digit2 = int(str2[j]) if j >= 0 else 0
        
        total = digit1 + digit2 + carry
        res = str(total % 2) + res
        carry = total // 2
        
        i -= 1
        j -= 1
        
    return res
