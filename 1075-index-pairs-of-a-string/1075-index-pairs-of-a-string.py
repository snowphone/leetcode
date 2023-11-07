from bisect import bisect_left

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        def search(word: str):
            i = bisect_left(words, word)
            return i < len(words) and words[i] == word
        
        words.sort()
        n = len(text)
        return [
            [i, j]
            for i in range(n)
            for j in range(i, n)
            if search( text[i:j+1] )
        ]

