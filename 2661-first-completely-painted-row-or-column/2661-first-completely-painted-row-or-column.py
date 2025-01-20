Matrix = Annotated[list[list[int]], ...]

class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: Matrix) -> int:
        nrow = len(mat)
        ncol = len(mat[0])

        def sort_by_order(mat: Matrix, arr: list[int]):
            new_map = {idx: new_idx for new_idx, idx in enumerate(arr)}
            mat = mat
            for r in range(nrow):
                for c in range(ncol):
                    mat[r][c] = new_map[mat[r][c]]
            return

        def calculate(mat: Matrix):
            ans = 987654321
            for line in mat:  # row
                ans = min(ans, max(line))
            for c in range(ncol):  # column
                ans = min(ans, max(mat[r][c] for r in range(nrow)))
            return ans

        sort_by_order(mat, arr)
        return calculate(mat)
