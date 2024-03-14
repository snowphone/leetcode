from bisect import bisect_right

class Solution:
    def psum(self, nums: list[int]):
        psum = nums[:1]
        for it in nums[1:]:
            psum.append(psum[-1] + it)
        return psum

    def bigger_cnt(self, nums: list[int], it: int):
        'nums must be sorted'
        n = len(nums)
        i = bisect_right(nums, it)
        return n - i

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        psum[i..j] == goal 
        psum[..j] - psum[i-1] == goal
        psum[i-1] + goal == psum[..j]
        """
        psum = self.psum(nums)
        rmap = defaultdict(list)
        for i, v in enumerate(psum):
            rmap[v].append(i)

        answer = 0
        n = len(nums)
        for i in range(-1, n):
            it = psum[i] if i >= 0 else 0
            jt = goal + it
            if jt in rmap:
                js = rmap[jt]
                answer += self.bigger_cnt(js, i)

        return answer

