class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        graph = {i: [] for i in range(numCourses) }
        for f, t in prerequisites:
            graph[f].append(t)
        
        @cache
        def reachable(node: int, target: int):
            if node == target:
                return True
            return any(
                adj == target or reachable(adj, target)
                for adj in graph[node]
            )

        return [
            reachable(f, t) for f, t in queries
        ]
        