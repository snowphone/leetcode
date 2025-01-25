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
        
        rows = {r: 0 for r in range(nrow)}
        cols = {c: 0 for c in range(ncol)}
        for r, c in nodes:
            rows[r] += 1
            cols[c] += 1
        
        adjacents = {(r, c): rows[r] > 1 or cols[c] > 1 for (r, c) in nodes}
        return adjacents