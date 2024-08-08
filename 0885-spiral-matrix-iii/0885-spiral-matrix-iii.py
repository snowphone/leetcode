class Delta:
    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1),  # Left
        (-1, 0),  # Up
    ]

    def __init__(self):
        self.direction = self.directions[0]
        self.same_direction_cnt = 0  # invariant: cnt < limit
        self.same_direction_limit = 1
        self.limit_cnt = 1
        return

    def next(self):
        self.same_direction_cnt += 1

        if self.same_direction_cnt == self.same_direction_limit:
            self.same_direction_cnt = 0
            self.limit_cnt += 1

            idx = self.directions.index(self.direction)
            self.direction = self.directions[(idx + 1) % len(self.directions)]

        if self.limit_cnt > 2:
            self.limit_cnt = 1
            self.same_direction_limit += 1

        return self.direction


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        sz = rows * cols

        answer = []

        r = rStart
        c = cStart
        delta = Delta()
        i = 1
        while i <= sz:
            if 0 <= r < rows and 0 <= c < cols:
                answer.append([r, c])
                i += 1

            dr, dc = delta.direction
            r += dr
            c += dc
            delta.next()

        return answer