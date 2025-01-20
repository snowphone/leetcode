from bisect import bisect_left

class ColWise:
    def __init__(self, mat):
        self.mat = mat
        self.nrow = len(mat)
        self.ncol = len(mat[0])
    
    def __getitem__(self, row_idx):
        return self.mat[row_idx][-1]
    
    def __len__(self):
        return len(self.mat[0])

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow = len(matrix)
        ncol = len(matrix[0])

        r = bisect_left(ColWise(matrix), target)
        if r < 0:
            r = 0
        if r == nrow:
            r = -1
        
        c = bisect_left(matrix[r], target)
        return 0 <= c < ncol and matrix[r][c] == target
    