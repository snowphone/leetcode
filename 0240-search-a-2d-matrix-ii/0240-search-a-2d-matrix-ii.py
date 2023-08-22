from bisect import bisect_left

class Solution:
    def bsearch(self, line, target):
        idx = bisect_left(line, target)
        return idx < len(line) and line[idx] == target

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        'Time Complexity: O(m lg(n) )'
        n_row = len(matrix)  # m
        n_col = len(matrix[0])  # n

        return any(
            self.bsearch(line, target) for line in matrix
        )

