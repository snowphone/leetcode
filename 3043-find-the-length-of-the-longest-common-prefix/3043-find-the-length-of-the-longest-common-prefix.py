class Trie:
    def __init__(self, words: list[str]):
        self.root = {}
        self.terminal = object()
        for word in words:
            self.add(word)
        return

    def add(self, word: str):
        nd = self.root
        for ch in word:
            nd = nd.setdefault(ch, {})
        nd[self.terminal] = True

    def longest_match(self, word: str):
        nd = self.root
        for i, ch in enumerate(word):
            if ch not in nd:
                return i
            nd = nd[ch]

        return len(word)

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie(map(str, arr1))

        return max(
            map(
                trie.longest_match,
                map(str, arr2)
            )
        )