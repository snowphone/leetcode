class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        answer = nums[:]  # Shallow copy

        for _ in range(k):
            i = min(
                enumerate(answer), key=lambda pair: [pair[1], pair[0]]
            )[0]
            answer[i] = answer[i] * multiplier
        return answer
