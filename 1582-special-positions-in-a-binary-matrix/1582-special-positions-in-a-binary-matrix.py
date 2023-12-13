class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n_row= len(mat)
        n_col = len(mat[0])

        def okay(r, c):
            for i in range(n_row):
                if i == r:
                    continue
                
                if mat[i][c] == 1:
                    return False

            for j in range(n_col):
                if j == c:
                    continue
                
                if mat[r][j] == 1:
                    return False
            return True
                    


        count = 0
        for r in range(n_row):
            for c in range(n_col):
                if mat[r][c] == 0:
                    continue
                
                if not okay(r, c):
                    continue
                count += 1
        return count
                
