from collections import Counter

def normalize(s: str):
    normalized = []
    mapping = dict()
    last = -1
    for ch in s:
        if ch not in mapping:
            last += 1
            mapping[ch] = last
        normalized.append(mapping[ch])
    return normalized
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        return normalize(s) == normalize(t)