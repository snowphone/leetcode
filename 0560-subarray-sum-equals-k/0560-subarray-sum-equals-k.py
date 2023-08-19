class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        @cache
        def acc(i: int):
            'Accumulate 0..i, inclusive'
            if i == 0:
                return nums[0]
            return acc(i-1) + nums[i]

        answer = 0
        n = len(nums)
        cnt = defaultdict(int)  # sum: cnt
        cnt[0] = 1
        for j in range(n):
            if acc(j) - k in cnt:  # i such that sum(j) - sum(i) == k exists!
                answer += cnt[acc(j) - k]
            cnt[acc(j)] += 1
        
        return answer