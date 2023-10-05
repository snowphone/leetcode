class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        acc = 0
        m = defaultdict(int)
        m[0] = 1

        for it in nums:
            acc += it
            cnt += m[acc - k]

            m[acc] += 1
        return cnt
        