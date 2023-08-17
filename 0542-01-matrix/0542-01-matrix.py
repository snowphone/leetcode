from queue import SimpleQueue

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n_row = len(mat)
        n_col = len(mat[0])

        answer = [[None for _ in range(n_col)] for _ in range(n_row)]
        counter = n_row * n_col


        q = SimpleQueue()

        for r in range(n_row):
            for c in range(n_col):
                if mat[r][c] != 0:
                    continue
                q.put( (r, c, 0) )

        while not q.empty():
            r, c, step = q.get()

            if answer[r][c] is not None:
                continue
            answer[r][c] = step
            counter -= 1

            if not counter:
                break
            

            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + i, c + j
                if not (0 <= nr < n_row):
                    continue
                if not (0 <= nc < n_col):
                    continue
                q.put( (nr, nc, step + 1) )
        
        return answer