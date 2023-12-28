class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def f(i, cur_ch, run_length, k):
            if k >= len(s)-i: 
                return 0
    
            # Keep s[i]
            if s[i] == cur_ch:
                ans = f(i + 1, cur_ch, run_length + 1, k)
                if run_length == 1 or len(str(run_length + 1)) > len(str(run_length)):
                    ans += 1
            else:
                ans = 1 + f(i + 1, s[i], 1, k)
    
            # Delete s[i]
            if k > 0:
                ans = min(ans, f(i + 1, cur_ch, run_length, k - 1))
    
            return ans
    
        return f(0, '', 0, k)