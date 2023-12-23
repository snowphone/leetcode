class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}

        prev = (0, 0)
        for it in path:
            x, y = prev
            match it:
                case 'N': new = (x, y+1)
                case 'S': new = (x, y-1)
                case 'W': new = (x-1, y)
                case 'E':  new = (x+1, y)
                case _: raise RuntimeError()
            
            if new in visited:
                return True
            visited.add(new)
            prev = new
        return False