from bisect import bisect_left

class Trie:
    TERMINAL = '$'
    def __init__(self):
        self.root = dict()

    def add(self, word):
        nd = self.root
        for ch in word:
            nd = nd.setdefault(ch, {})
        nd[self.TERMINAL] = True
        return
    
    def find(self, word):
        nd = self.root
        for ch in word:
            if ch not in nd:
                return False
            nd = nd[ch]

        return nd.get(self.TERMINAL) == True


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for word in words:
            trie.add(word)
        
        n = len(text)
        return [
            [i, j]
            for i in range(n)
            for j in range(i, n)
            if trie.find( text[i:j+1] )
        ]

