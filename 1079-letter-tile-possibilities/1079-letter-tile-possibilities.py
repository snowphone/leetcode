from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return len(self.gen(tiles))
    
    def gen(self, tiles: list[str]):
        if len(tiles) == 1:
            return { tuple(tiles) }
        
        answer = set()
        for i, ch in enumerate(tiles):
            popped = [it for j, it in enumerate(tiles) if j != i]
            subanswer = self.gen(popped)
            answer |= subanswer
            answer |= set( (ch, *jt) for jt in subanswer )

        return answer