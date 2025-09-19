from collections import defaultdict

def total_fruit(fruits):
    fruit_counts = defaultdict(int)
    max_fruits = 0
    left = 0
    
    for right in range(len(fruits)):
        fruit_counts[fruits[right]] += 1
        
        while len(fruit_counts) > 2:
            fruit_to_remove = fruits[left]
            fruit_counts[fruit_to_remove] -= 1
            if fruit_counts[fruit_to_remove] == 0:
                del fruit_counts[fruit_to_remove]
            left += 1
            
        max_fruits = max(max_fruits, right - left + 1)
        
    return max_fruits
