class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        indegree = defaultdict(int)
        for f, t in roads:
            indegree[f] += 1
            indegree[t] += 1
        

        answer = 0
        for i in range(n):
            for j in range(i+1, n):
                if [i,j] in roads or [j, i] in roads:
                    tmp = indegree[i] + indegree[j] - 1
                else:
                    tmp = indegree[i] + indegree[j]
                answer = max(answer, tmp)

        return answer