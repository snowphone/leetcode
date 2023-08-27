class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]; fast = nums[0]
        nxt = lambda it: nums[it]

        while fast and nxt(fast):
            slow = nxt(slow)
            fast = nxt(nxt(fast))

            if slow == fast:
                slow = nums[0]
                while slow != fast:
                    slow = nxt(slow)
                    fast = nxt(fast)
                return slow
        return -1
