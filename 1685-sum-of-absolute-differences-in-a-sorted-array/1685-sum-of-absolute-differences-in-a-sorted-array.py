class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)

        acc = [0] + nums
        for i in range(1, len(acc)):
            acc[i] += acc[i-1]

        def rangesum(b, e):
            "Accumulate elements at [b, e)"
            return acc[e] - acc[b]

        answer = []
        for i in range(n):
            answer.append(
                -rangesum(0, i) + rangesum(i+1, n) + nums[i] * (i - ( n - ( i + 1) ) )
            )
        return answer