class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        nums = [it for line in bank if (it := line.count('1'))]
        print(nums)

        return sum(
            it * jt
            for it, jt in zip(nums, nums[1:])
        )
