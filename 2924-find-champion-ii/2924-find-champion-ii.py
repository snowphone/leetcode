class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = {it: 0 for it in range(n)}
        for _, t in edges:
            indegree[t] += 1
        
        champions = [it for it in range(n) if indegree[it] == 0]
        
        if len(champions) != 1:
            return -1
        return champions[0]
        