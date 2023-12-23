class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}

        prev = (0, 0)
        for it in path:
            x, y = prev
            if it == 'N':
                new = (x, y+1)
            elif it == 'S':
                new = (x, y-1)
            elif it == 'W':
                new = (x-1, y)
            elif it == 'E':
                new = (x+1, y)
            
            if new in visited:
                return True
            visited.add(new)
            prev = new
        return False