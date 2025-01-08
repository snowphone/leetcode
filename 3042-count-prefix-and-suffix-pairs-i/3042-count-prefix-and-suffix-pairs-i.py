class Trie:
    def __init__(self):
        self.terminal = object()
        self.root = {}
    
    def add(self, word: str):
        nd = self.root
        for ch in word:
            nd = nd.setdefault(ch, {})
        nd[self.terminal] = True
    
    def starts_with(self, word: str):
        nd = self.root
        for ch in word:
            if ch not in nd:
                return False
            nd = nd[ch]
        return True


class SuffixTrie(Trie):
    def add(self, word: str):
        super().add(word[::-1])
    
    def starts_with(self, word: str):
        return super().starts_with(word[::-1])

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        answer = 0

        for j in range(n):
            prefix_trie = Trie()
            suffix_trie = SuffixTrie()
            word = words[j]
            prefix_trie.add(word)
            suffix_trie.add(word)

            for i in range(j):
                fix = words[i]
                if prefix_trie.starts_with(fix) and suffix_trie.starts_with(fix):
                    answer += 1

        return answer
