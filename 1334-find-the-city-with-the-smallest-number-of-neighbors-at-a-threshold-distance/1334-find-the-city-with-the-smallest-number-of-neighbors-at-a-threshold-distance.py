class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        INF = 987654321
        
        distances = [[INF] * n for _ in range(n)]
        for f, t, w in edges:
            distances[f][t] = w
            distances[t][f] = w
        for i in range(n):
            distances[i][i] = 0

        # Floyd Warshall algorithm
        for stopover in range(n):
            for f in range(n):
                for t in range(n):
                    detour_cost = distances[f][stopover] + distances[stopover][t]
                    distances[f][t] = min(distances[f][t], detour_cost)

        return min(
            (i for i in range(n - 1, -1, -1)),
            key=lambda i: sum(1 for it in distances[i] if it <= distanceThreshold),
        )
