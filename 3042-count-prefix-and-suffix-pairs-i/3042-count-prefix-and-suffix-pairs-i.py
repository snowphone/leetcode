class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        answer = 0
        for i, fix in enumerate(words):
            for j in range(i+1, n):
                word = words[j]
                if word.startswith(fix) and word.endswith(fix):
                    answer += 1
        return answer