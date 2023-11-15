class Solution:
    def countHomogenous(self, s: str) -> int:
        "Time complexity: O( n log(n) )"
        MOD = 10 ** 9 + 7
        
        def divide_and_conquer(b, e):
            n = e - b
            if n == 0:
                return 0
            if n == 1:
                return 1

            m = (b + e) // 2
            left = divide_and_conquer(b, m)
            right = divide_and_conquer(m, e)

            if s[m-1] != s[m]:
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
            return (left + right + cnt) % MOD
        
        return divide_and_conquer(0, len(s))
