class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        acc = 0

        # key: sum(nums[:i+1])
        # value: if not zero, it stands for s(i) exists such that s(j) - s(i) = k <=> sum(nums[i+1:j+1]) = k
        #                     and there's `value` i's exist.
        m = defaultdict(int)
        m[0] = 1  # To count myself

        for it in nums:
            acc += it
            cnt += m[acc - k]

            m[acc] += 1
        return cnt
        