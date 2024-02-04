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
                    answer = s[l:r+1]
                else:
                    answer = min(
                        answer,
                        s[l:r+1],
                        key=len,
                    )
                window[s[l]] -= 1
                l += 1
                
        return answer if answer is not None else ''


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