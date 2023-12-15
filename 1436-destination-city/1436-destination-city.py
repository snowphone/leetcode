class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        froms = set()
        tos = set()

        for f, t in paths:
            froms.add(f)
            tos.add(t)
        return next(iter(tos - froms))