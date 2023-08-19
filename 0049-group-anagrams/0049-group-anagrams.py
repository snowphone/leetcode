class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        for s in strs:
            counter[''.join(sorted(s))].append(s)
        return list(counter.values())