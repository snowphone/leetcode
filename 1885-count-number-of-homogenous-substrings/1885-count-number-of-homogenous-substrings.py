class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        
        def divconq(b, e):
            n = e - b
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                # print(f"{b} to {e}: {s[b] == s[b+1] = }")
                return 3 if s[b] == s[b+1] else 2
            m = (b + e) // 2
            left = divconq(b, m)
            right = divconq(m, e)

            if s[m-1] != s[m]:
                # print(f"{b} to {e}: {left}, {right}")
                return (left + right) % MOD

            l = m-1
            r = m
            while s[l] == s[r]:
                changed = False
                if l != b and s[l] == s[l-1]:
                    l -= 1
                    changed = True

                if r != e - 1 and s[r] == s[r+1]:
                    r += 1
                    changed = True
                
                if not changed:
                    break
            cnt = (m - l) * (r - (m - 1))
            # print(f"{b} to {e}: {left}, {right}, {(l, r) = }, {cnt}")
            return (left + right + cnt) % MOD
        
        return divconq(0, len(s))
