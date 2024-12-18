class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def solve(b: int, e: int):
            match e-b:
                case 0: return 0
                case 1: return nums[b]
                case 2: return max(nums[b], nums[b+1], sum(nums[b:e]))
            m = (b + e) // 2
            candidates = [ solve(b, m), solve(m, e) ]

            left_max, acc = nums[m-1], 0
            for i in range(m-1, b-1, -1):
                acc += nums[i]
                left_max = max(acc, left_max)

            right_max, acc = nums[m], 0
            for i in range(m, e):
                acc += nums[i]
                right_max = max(acc, right_max)
            return max(*candidates, left_max + right_max)
        
        return solve(0, len(nums))
