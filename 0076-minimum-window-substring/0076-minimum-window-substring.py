from collections import Counter

class Solution:
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" "abcdefghijklmnopqrstuvwxyz"

    def minWindow(self, s: str, t: str) -> str:
        """
        until all chars are in the substr:
            go forward
        while still valid substr:
            retreat

        Time Complexity:
             O(m + n) where m is the length of the string `s` and n is the length of the string `t`
        """
        tcnt = Counter(t)
        window = {ch: 0 for ch in self.ALPHABET}

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
            cnt <= window[ch]
            for ch, cnt in tcnt.items()
        )
