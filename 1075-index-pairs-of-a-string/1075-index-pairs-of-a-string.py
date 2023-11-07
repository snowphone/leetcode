class Trie:
    TERMINAL = "$"

    def __init__(self, needle):
        self.root = dict()
        self.needle = needle

    def add(self, word):
        nd = self.root
        for ch in word:
            nd = nd.setdefault(ch, {})
        nd[self.TERMINAL] = True
        return

    def find_all(self, beg):
        answer = []
        nd = self.root
        for i in range(beg, len(self.needle)):
            ch = self.needle[i]

            if self.TERMINAL in nd:
                answer.append([beg, i - 1])
            if ch not in nd:
                return answer
            nd = nd[ch]

        if self.TERMINAL in nd:
            answer.append([beg, len(self.needle) - 1])
        return answer


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie(text)
        for word in words:
            trie.add(word)

        n = len(text)
        answer = []
        for i in range(n):
            answer += trie.find_all(i)
        return answer