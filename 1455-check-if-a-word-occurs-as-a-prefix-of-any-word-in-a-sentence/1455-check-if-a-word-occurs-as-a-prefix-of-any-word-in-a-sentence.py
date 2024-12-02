class Trie:
    def __init__(self):
        self.root = {}
        self.terminal = object()

    def add(self, word: str, index: int):
        nd = self.root
        for ch in word:
            nd.setdefault(ch, {})
            nd = nd[ch]
        nd[self.terminal] = index
        return
    
    def find(self, prefix: str) -> int|None:
        nd = self.root
        for ch in prefix:
            if ch not in nd:
                return None
            nd = nd[ch]
        inf = 987654321
        idx = self._find_min(nd, inf)
        if idx != inf:
            return idx
        return None
    
    def _find_min(self, nd, current_min):
        for key, value in nd.items():
            if key == self.terminal:
                current_min = min(current_min, value) # Value is an index
            else:
                current_min = min(current_min, self._find_min(value, current_min)) # Value is a node
        return current_min

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        trie = Trie()
        riter = list(enumerate(sentence.split(' ')))[::-1]
        for i, word in riter:
            trie.add(word, i)
        
        if (idx := trie.find(searchWord)) is None:
            return -1
        return idx + 1
