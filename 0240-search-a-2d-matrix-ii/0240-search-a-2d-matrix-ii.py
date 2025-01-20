from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow = len(matrix)
        ncol = len(matrix[0])
        r, c = nrow-1, 0

        def get(r, c):
            if r < 0:
                return -987654321
            if c >= ncol:
                return 9876543221
            return matrix[r][c]

        while r >= 0 or c < ncol:
            me = get(r, c)

            if target == me:
                return True
            elif target > me:
                c += 1
            else:
                r -= 1
        return False
                
