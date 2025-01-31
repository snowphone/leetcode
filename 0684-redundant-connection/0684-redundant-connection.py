class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        for f, t in edges:
            if self._connected(f, t, {f}):
                return [f, t]
            self.graph[t].append(f)
            self.graph[f].append(t)
    
    def _connected(self, node: int, target: int, visited: set[int]):
        """
        If it has a cycle, it has a path from a node to the target
        even there's no direct edge between node and target.
        """
        answer = False
        for adj in self.graph[node]:
            if adj == target:
                return True
            if adj in visited:
                continue 
            visited.add(adj)
            answer = answer or self._connected(adj, target, visited)

        return answer
