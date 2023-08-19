
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        positions = defaultdict(list)
        for i, ch in enumerate(s):
            positions[ch].append(i)
        
        # List-ify
        parts = [(min(vals), max(vals)) for vals in positions.values()]
        parts.sort()
        
        # Merge
        merged = parts[:1]
        for fir, last in parts[1:]:
            if fir <= merged[-1][1]:
                merged[-1] = (min(merged[-1][0], fir ), max(merged[-1][1], last) )
            else:
                merged.append((fir, last))
        
        return [r - l + 1 for l, r in merged]