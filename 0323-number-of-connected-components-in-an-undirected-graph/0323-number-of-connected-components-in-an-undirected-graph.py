class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(prev, nd, visited):
            for adj in graph[nd]:
                if adj in [prev, nd]:
                    continue
                
                if adj in visited:
                    continue
                visited.add(adj)
                dfs(nd, adj, visited)

            return visited

        cnt = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            visited |= dfs(None, i, {i})
            cnt += 1
        return cnt

        