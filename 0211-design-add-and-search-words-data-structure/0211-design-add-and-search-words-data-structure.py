class Trie:
    TERMINAL = '$'
    def __init__(self):
        self.root = dict()
        return
    
    def add(self, word: str):
        self._add(word, self.root)
        return 

    def _add(self, word: str, root: dict):
        nd = root
        for ch in word:
            nd = nd.setdefault(ch, dict())
        nd[self.TERMINAL] = self.TERMINAL
        return 

    def _search(self, word: str, root: dict):
        nd = root
        for i, ch in enumerate(word):
            if ch == '.':
                subword = word[i+1:]
                return any(self._search(subword, v) for v in nd.values() if v != self.TERMINAL)
            if ch not in nd:
                return False
            nd = nd[ch]
        return self.TERMINAL in nd
    
    def __contains__(self, word: str):
        return self._search(word, self.root)

class WordDictionary:
    def __init__(self):
        self.items = Trie()

    def addWord(self, word: str) -> None:
        self.items.add(word)

    def search(self, word: str) -> bool:
        return word in self.items
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)