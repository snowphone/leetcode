class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10 ** 10 + 7
        costs = defaultdict(lambda: defaultdict(lambda: INF))

        nodes = set()
        for f, t, c in zip(original, changed, cost):
            costs[f][t] = min(costs[f][t], c)
            nodes |= {f, t}
        
        for node in nodes:
            costs[node][node] = 0

        # Floyd-Warshall
        for stopover in nodes:
            for f in nodes:
                for t in nodes:
                    costs[f][t] = min(
                        costs[f][t],
                        costs[f][stopover] + costs[stopover][t]
                    )
        
        answer = 0
        for f, t in zip(source, target):
            if costs[f][t] == INF:
                return -1
            answer += costs[f][t]
        return answer