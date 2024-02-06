from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        @cache
        def key(s):
            return sorted(s)
        
        return [
            list(group)
            for k, group in groupby(sorted(strs, key=key), key=key)
        ]