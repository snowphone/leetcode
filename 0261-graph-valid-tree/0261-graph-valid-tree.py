class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        1. Acyclic
        2. Visit all nodes
        """
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        

        def dfs(prev, nd, visited): 
            for adj in graph[nd]:
                if adj in [nd, prev]:
                    continue
                if adj in visited:
                    return None
                
                visited.add(adj)
                if dfs(nd, adj, visited) is None:
                    return None
            return visited
        
        return (it := dfs(None, 0, {0}) ) is not None and len(it) == n
