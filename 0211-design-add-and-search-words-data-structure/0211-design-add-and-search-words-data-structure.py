from sortedcontainers import SortedSet

class WordDictionary:
    def __init__(self):
        self.items = SortedSet()

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