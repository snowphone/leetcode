from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        'Time Complexity: O( m + n )'
        n_row = len(matrix)  # m
        n_col = len(matrix[0])  # n

        r = 0
        c = n_col - 1
        while r < n_row and 0 <= c:
            it = matrix[r][c]
            print(it)
            if it == target:
                return True
            if it > target:
                c -= 1
            else:
                r += 1
        return False

