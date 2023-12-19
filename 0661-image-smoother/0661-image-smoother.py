from math import floor
from statistics import mean
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        self.img = img

        n_row = len(img)
        n_col = len(img[0])

        answer = [[0 for _ in range(n_col)] for _ in range(n_row)]

        for r in range(n_row):
            for c in range(n_col):
                answer[r][c] = self.avg(r, c)
        return answer

    def avg(self, r: int, c: int) -> int:
        img = self.img
        n_row = len(img)
        n_col = len(img[0])

        nums = []
        for i, j in [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]:
            if not (0 <= r + i < n_row):
                continue
            if not (0 <= c + j < n_col):
                continue
            nums.append(img[r + i][c + j])

        return floor(mean(nums))