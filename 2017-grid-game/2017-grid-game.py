class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        def calc_pf(line: list[int]):
            prev, pf = 0, []
            for it in line:
                pf.append(prev + it)
                prev = pf[-1]
            return pf

        pf1 = calc_pf(grid[0])
        pf2 = calc_pf(grid[1])
        pf2.append(0)  # pf2[-1] == sum of [0, 0)

        @cache
        def robot2_goes_down_at(i: int):
            return max(
                (pf1[-1] - pf1[i]),  # Robot2 chooses row 0
                pf2[i - 1],  # Robot2 chooses row 1
            )

        n = len(grid[0])
        min_idx = min(
            (i for i in range(n)),
            key=lambda i: robot2_goes_down_at(i),
        )

        return robot2_goes_down_at(min_idx)
