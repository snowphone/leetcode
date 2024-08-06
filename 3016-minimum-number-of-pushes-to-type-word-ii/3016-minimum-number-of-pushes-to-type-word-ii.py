from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Given eight slots, 
        counter = Counter(word)
        costmap = { ch: 0 for ch in counter.keys() }

        cost = 1
        order = sorted(counter.items(), key=lambda it: it[1], reverse=True)
        for i in range(0, len(order), 8):
            for ch, _ in order[i:min(i+8, len(order))]:
                costmap[ch] = cost
            cost += 1
        
        return sum(
            costmap[ch] * cnt for ch, cnt in order
        )