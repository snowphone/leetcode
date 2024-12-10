class Solution:
    def maximumLength(self, s: str) -> int:
        # key: (char, length)
        # value: count
        counter = defaultdict(int)

        def make_special(ch: str, sz: int):
            for i in range(1, sz + 1):
                counter[(ch, i)] += sz + 1 - i
            return

        i, n = 0, len(s)
        while i < n:
            j = next((k for k in range(i, n) if s[k] != s[i]), n)
            make_special(s[i], j - i)
            i = j

        candidates = [k[1] for k, v in counter.items() if v >= 3]

        if not candidates:
            return -1
        return max(candidates)
