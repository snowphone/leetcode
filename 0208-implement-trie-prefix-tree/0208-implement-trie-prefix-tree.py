class Trie:
    EXISTS = object()
    def __init__(self):
        self.root = dict()
        
    def insert(self, word: str) -> None:
        nd = self.root
        for ch in word:
            nd = nd.setdefault(ch, dict())
        nd[self.EXISTS] = True

    def search(self, word: str) -> bool:
        nd = self.root
        for ch in word:
            if ch not in nd:
                return False
            nd = nd[ch]
        return nd.get(self.EXISTS, False)

    def startsWith(self, prefix: str) -> bool:
        nd = self.root
        for ch in prefix:
            if ch not in nd:
                return False
            nd = nd[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)