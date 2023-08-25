class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 1
        curr = nums[0]
        for n in nums[1:]:
            if curr == n:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    cnt = 1
                    curr = n
        return curr

        