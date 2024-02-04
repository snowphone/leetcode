from collections import Counter

class Solution:
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" "abcdefghijklmnopqrstuvwxyz"

    def minWindow(self, s: str, t: str) -> str:
        """
        until all chars are in the substr:
            go forward
        while still valid substr:
            retreat
        """
        tcnt = self._make_counter(t)
        window = self._make_counter(None)

        l = 0
        answer = None
        for r, ch in enumerate(s):
            window[ch] += 1

            while self._valid(tcnt, window):
                if answer is None:
                    answer = (l, r)
                else:
                    answer = min(
                        answer,
                        (l, r),
                        key=lambda it: it[1] - it[0] + 1,
                    )
                window[s[l]] -= 1
                l += 1
                
        if answer:
            l, r = answer
            return s[l:r+1]
        else:
            return ""


    def _valid(self, tcnt: dict[str, int], window: dict[str, int]):
        return all(
            tcnt[ch] <= window[ch]
            for ch in self.ALPHABET
        )
        
    def _make_counter(self, obj: str|None):
        cnt = {ch: 0 for ch in self.ALPHABET}

        if obj and isinstance(obj, str):
            for ch in obj:
                cnt[ch] += 1
        return cnt