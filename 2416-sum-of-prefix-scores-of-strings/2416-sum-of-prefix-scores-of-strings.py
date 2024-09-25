class Trie:
    def __init__(self, words: Iterable[str]):
        self.terminal = object()
        self.root = {}  # ch -> [nd, cnt]
        for word in words:
            self.add(word)
        return

    def add(self, word: str):
        nd = self.root
        for ch in word:
            nd.setdefault(ch, [{}, 0])
            nd[ch][1] += 1
            nd = nd[ch][0]
        return
    
    def count(self, word: str):
        nd = self.root
        cnt = 0
        for ch in word:
            if ch not in nd:
                return 0
            cnt += nd[ch][1]
            nd = nd[ch][0]
        
        return cnt
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie(words)
        return [ trie.count(it) for it in words ]
