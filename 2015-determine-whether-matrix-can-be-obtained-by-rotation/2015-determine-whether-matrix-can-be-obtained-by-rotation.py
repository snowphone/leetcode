class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if _equals(mat, target):
                return True
            _rotate(mat)

        return False

def _equals(lhs, rhs):
    return all(it == jt for it, jt in zip(lhs, rhs) )
    
def _rotate(mat):
    n_row = len(mat)
    n_col = len(mat[0])

    _transpose(mat)
    for line in mat:
        line.reverse()
    return

def _transpose(mat):
    n_row = len(mat)
    n_col = len(mat[0])

    for r in range(n_row):
        for c in range(r+1, n_col):
            mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
    return