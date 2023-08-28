from collections import Counter
from string import ascii_lowercase

class Solution:
    def create_dict(self, s: str = ""):
        cnt = dict()
        for ch in ascii_lowercase:
            cnt[ch] = 0
        for ch in s:
            cnt[ch] += 1
        return cnt

    def findAnagrams(self, s: str, p: str) -> List[int]:
        base = self.create_dict(p)
        cnt = self.create_dict()
        left = 0
        answer = []
        sz = lambda: right - left + 1
        for right, ch in enumerate(s):
            cnt[ch] += 1
            while sz() > len(p):
                ch1 = s[left]
                cnt[ch1] -= 1
                left += 1
            if base == cnt:
                answer.append(left)
        return answer
        
        