from itertools import chain

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        adjacents = self._get_graph(grid)
            
        return sum(
            1 for node in adjacents.keys() if adjacents[node]
        )
    
    def _get_graph(self, grid: list[list[int]]):
        adjacents = dict()
        nrow = len(grid)
        ncol = len(grid[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        nodes = set()
        for r in range(nrow):
            for c in range(ncol):
                if not grid[r][c]:
                    continue
                node = (r, c)
                nodes.add( node )
                rows[r].add( node )
                cols[c].add( node )

        for node in nodes:
            r, c = node
            adjacents[node] = (rows[r] | cols[c]) - {node}
        return adjacents