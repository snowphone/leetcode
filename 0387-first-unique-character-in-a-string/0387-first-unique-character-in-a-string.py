class Solution:
    def firstUniqChar(self, s: str) -> int:
        indices_map = defaultdict(list)

        for i, ch in enumerate(s):
            indices_map[ch].append(i)
        
        for indices in indices_map.values():
            if len(indices) == 1:
                return indices[0]
        return -1