class Trie:
    TERMINAL = object()
    def __init__(self):
        self.root = dict()
        return
    
    def add(self, word: str):
        nd = self.root
        for ch in word:
            nd = nd.setdefault(ch, dict())
        nd[self.TERMINAL] = self.TERMINAL
        return 

    def search(self, word: str):
        nd = self.root
        for ch in word:
            if ch not in nd:
                return False
            nd = nd[ch]
        return self.TERMINAL in nd
    
    def __contains__(self, word: str):
        return self.search(word)

class WordDictionary:
    def __init__(self):
        self.items = Trie()

    def addWord(self, word: str) -> None:
        self.items.add(word)

    def search(self, word: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        cnt = word.count('.')
        if cnt == 1:
            return any(
                word.replace('.', ch) in self.items
                for ch in alphabet
            )
        if cnt == 2:
            return any(
                word.replace('.', ch, 1).replace('.', dh) in self.items
                for ch in alphabet 
                for dh in alphabet
            )
        return word in self.items
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)