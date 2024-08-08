class Delta:
    """
    이동 방향은 그 위치에 숫자를 적을 수 있는지 없는지와는
    무관하게 아래의 규칙에 따라서 움직인다.
    R D
    L L U U
    R R R D D D
    L L L L U U U U
    """
    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1),  # Left
        (-1, 0),  # Up
    ]

    def __init__(self):
        self.direction = self.directions[0]
        self.same_direction_cnt = -1  # invariant: cnt < limit
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

            dr, dc = delta.next()
            r += dr
            c += dc
            #delta.next()

        return answer