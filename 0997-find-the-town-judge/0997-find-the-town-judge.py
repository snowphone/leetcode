class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustmap = defaultdict(list)
        trustcnt = defaultdict(int)

        for truster, trustee in trust:
            trustmap[trustee].append(truster)
            trustcnt[truster] += 1
        
        for i in range(1, n+1):
            if len(trustmap[i]) != n-1:
                continue
            
            if trustcnt[i] == 0:
                return i
        return -1
            
        
