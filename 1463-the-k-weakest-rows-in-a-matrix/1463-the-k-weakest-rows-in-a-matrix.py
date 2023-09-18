class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        key = lambda i: (mat[i].count(1), i)

        indices = [i for i, _ in enumerate(mat)]
        indices.sort(key=key)

        return indices[:k]
        