from itertools import chain

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        adjacents = self._get_graph(grid)
            
        return sum( adj for node, adj in adjacents.items() )
    
    def _get_graph(self, grid: list[list[int]]):
        nrow = len(grid)
        ncol = len(grid[0])
        nodes = {
            (r, c)
            for r in range(nrow)
            for c in range(ncol)
            if grid[r][c]
        }
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        for node in nodes:
            r, c = node
            rows[r].add( node )
            cols[c].add( node )

        adjacents = {nd: False for nd in nodes}
        for node in nodes:
            r, c = node
            for adj in chain(rows[r], cols[c]):
                if adj == node:
                    continue
                adjacents[adj] = True

        return adjacents