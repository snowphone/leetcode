class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = sorted(wordDict)

        def find(needle, b = 0, e = len(words)):
            if e - b <= 2:
                return next((i for i in range(b, e) if words[i] == needle), -1)
            m = (b + e) // 2
            if words[m] < needle:
                return find(needle, m, e)
            if needle < words[m]:
                return find(needle, b, m)
            return m

        @cache
        def fn(s: str):
            if not s:
                return True
            for i in range(1, len(s) + 1):
                prefix = s[:i]
                idx = find(prefix)
                if idx == -1:
                    continue
                new_s = s[i:]
                if fn(new_s):
                    return True
            return False

        return fn(s)