class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(
            it[::-1] for it in s.split()
        )