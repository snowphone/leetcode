class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = [it for it in nums if it > 0]
        negatives = [it for it in nums if it < 0]

        answer = []
        for p, n in zip(positives, negatives):
            answer += [p, n]
        return answer