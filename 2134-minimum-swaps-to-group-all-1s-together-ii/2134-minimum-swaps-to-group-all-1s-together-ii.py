class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window_length = sum(nums)

        if window_length == 0:
            return 0

        answer = 987654321

        cnt = { 1: 0, 0: 0 }

        nums = nums + nums
        n = len(nums)
        l = 0
        for r in range(n-1):
            it = nums[r]
            cnt[it] += 1

            sz = lambda: r - l + 1
            while sz() > window_length:
                left_it = nums[l]
                cnt[left_it] -= 1
                l += 1
            
            answer = min(
                answer,
                window_length - cnt[1]
            )
        return answer


