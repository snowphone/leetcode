class Trie:
    def __init__(self, items: list[str] = []):
        self.root = {}
        self.TERMINAL = True

        for item in items:
            self.add(item)

    def add(self, item: str):
        nd = self.root
        for ch in item:
            nd = nd.setdefault(ch, {})
        nd[self.TERMINAL] = True
        return
    
    def find_all(self, word: str):
        nd = self.root
        for i, ch in enumerate(word):
            if self.TERMINAL in nd:
                yield word[:i]
            if ch not in nd:
                return
            nd = nd[ch]
        if self.TERMINAL in nd:
            yield word
        return

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wiki = Trie(dictionary)
        self.s = s
        self.wiki = wiki
        return self._solve(0)

    @cache
    def _solve(self, idx: int):
        'idx usage: search for s[idx:]'
        s, wiki = self.s, self.wiki
        if idx >= len(s):
            return 0
        candidates = wiki.find_all(s[idx:])
        
        return min(
            (
                1 + self._solve(idx + 1),
                *[self._solve(idx + len(cand)) for cand in candidates],
            )
        )