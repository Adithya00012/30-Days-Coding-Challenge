from collections import deque
import bisect

class MKAverage(object):
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.stream = deque()
        self.window = []  # Sorted window of last m elements
        
    def addElement(self, num):
        self.stream.append(num)
        
        # If we have more than m elements, remove the oldest
        if len(self.stream) > self.m:
            old_num = self.stream.popleft()
            # Remove from sorted window
            idx = bisect.bisect_left(self.window, old_num)
            self.window.pop(idx)
        
        # Add new element to sorted window
        if len(self.stream) <= self.m:
            bisect.insort(self.window, num)
    
    def calculateMKAverage(self):
        if len(self.stream) < self.m:
            return -1
        
        # Get middle elements (excluding k smallest and k largest)
        middle_elements = self.window[self.k:self.m - self.k]
        middle_sum = sum(middle_elements)
        middle_count = len(middle_elements)
        
        return middle_sum // middle_count
