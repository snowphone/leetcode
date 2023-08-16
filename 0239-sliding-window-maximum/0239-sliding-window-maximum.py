from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        left = 0
        window = SortedList()
        for right, n in enumerate(nums):
            window.add(n)

            if len(window) < k:
                continue
            while len(window) > k:
                n = nums[left]
                window.remove(n)
                left += 1

            answer.append(window[-1])
        return answer