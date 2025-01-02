class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pfsum = []
        acc = 0
        for word in words:
            if self._satisfies(word):
                acc += 1
            pfsum.append(acc)
        pfsum.append(0)  # pfsum[-1] = 0

        answer = []
        for l, r in queries:
            answer.append(pfsum[r] - pfsum[l - 1])
        return answer

    def _satisfies(self, word):
        vowels = "aeiou"
        return word[0] in vowels and word[-1] in vowels
