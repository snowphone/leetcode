DIRECTIONS = ["RIGHT", "DOWN", "LEFT", "UP"]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r_len = len(matrix)
        c_len = len(matrix[0])
        visited = [[False for _ in range(c_len)] for _ in range(r_len)]

        r = 0; c = 0
        r_inc = 0; c_inc = 1
        dir_idx = 0

        answer = []
        while 0 <= r < r_len and 0<= c < c_len and not visited[r][c]:
            answer.append(matrix[r][c])
            visited[r][c] = True

            dir = DIRECTIONS[dir_idx]
            if dir == "RIGHT" and (c + 1 == c_len or visited[r][c+1]):
                dir_idx = (dir_idx + 1) % 4
                r_inc = 1
                c_inc = 0
            elif dir == "DOWN" and (r + 1 == r_len or visited[r+1][c]):
                dir_idx = (dir_idx + 1) % 4
                r_inc = 0
                c_inc = -1
            elif dir == "LEFT" and (c - 1 == -1 or visited[r][c-1]):
                dir_idx = (dir_idx + 1) % 4
                r_inc = -1
                c_inc = 0
            elif dir == "UP" and visited[r-1][c]:
                dir_idx = (dir_idx + 1) % 4
                r_inc = 0
                c_inc = 1

            r += r_inc
            c += c_inc

        return answer