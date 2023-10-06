class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        def s(i): return sum(nums[:i+1])

        ( s(j) - s(i) ) % k == 0
         <=> s(j) % k == s(i) % k
        """
        n = len(nums)
        # key: s(i) % k
        # value: list of i
        m = defaultdict(list)
        m[0].append(-1)

        acc = 0
        for j, it in enumerate(nums):
            acc += it
            remainder = acc % k

            i = m[remainder][0] if m[remainder] else j
            if j - i >= 2:
                return True

            m[remainder].append(j)
        return False
