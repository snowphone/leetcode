class Trie:
    def __init__(self):
        self.terminal = object()
        self.root = {}

    def add(self, word: str):
        for i in range(len(word)):
            self._add(word[i:])
        return

    def _add(self, word: str):
        nd = self.root
        for ch in word:
            nd = nd.setdefault(ch, {})
        cnt = nd.setdefault(self.terminal, 0)
        nd[self.terminal] = cnt + 1
        return

    def contains(self, word: str):
        nd = self.root
        for ch in word:
            if ch not in nd:
                return False
            nd = nd[ch]
        if self.terminal in nd:
            return nd[self.terminal] > 1 or len(nd.keys()) > 1
        return True


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)

        return [word for word in words if trie.contains(word)]
