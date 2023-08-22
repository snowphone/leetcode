from collections import deque

class MQ(deque):
    'Monotonic Queue'

    def __init__(self, reverse=False):
        super().__init__()
        if reverse:
            self._key = lambda it: self[-1] < it
        else:
            self._key = lambda it: self[-1] > it
        return
    
    def add(self, item):
        while self and self._key(item):
            self.pop()
        self.append(item)
    
    def remove(self, item):
        if self[0] != item:
            return
        return self.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        'Time Complexity: O(n)'
        answer = []

        window = MQ(reverse=True)
        left = 0
        for right, it in enumerate(nums):
            window.add(it)
            while right - left + 1 > k:
                jt = nums[left]
                window.remove(jt)
                left += 1
            if right - left + 1 < k:
                continue
            answer.append(window[0])
            
        return answer