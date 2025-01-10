from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        @cache
        def freq(s: str):
            arr = [0 for _ in range(26)]
            for ch in s:
                arr[ord(ch) - ord('a')] += 1
            return arr

        def is_subset(big, small):
            return all(
                it <= jt for it, jt in zip(small, big)
            )
            return freq(big) >= freq(small)
        
        def universal(word):
            return is_subset(freq(word), create_intersection() )
        
        @cache
        def create_intersection():
            return [
                max(f) for f in zip(*map(freq, words2))
            ]

        return [
            word for word in words1 if universal(word)
        ]