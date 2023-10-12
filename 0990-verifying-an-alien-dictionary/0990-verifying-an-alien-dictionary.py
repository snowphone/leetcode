class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pri = {ch: i for i, ch in enumerate(order)}

        nums = [
            [pri[ch] for ch in word]
            for word in words
        ]

        return nums == sorted(nums)