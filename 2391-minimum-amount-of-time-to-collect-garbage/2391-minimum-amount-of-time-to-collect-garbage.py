class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        answer = 0
        for g in ["M", "P", "G"]:
            last_idx = next( (i for i in range(n-1, -1, -1) if g in garbage[i]), -1)

            for i in range(last_idx + 1):
                answer += garbage[i].count(g)
                if i != last_idx:
                    answer += travel[i]
                    
        return answer