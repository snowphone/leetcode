from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        'Time Complexity: O(n lg(k) )'
        answer = []

        window = SortedList()
        left = 0
        for right, it in enumerate(nums):
            window.add(it)
            while right - left + 1 > k:
                window.remove(nums[left])
                left += 1
            if right - left + 1 < k:
                continue
            answer.append(window[-1])
        return answer