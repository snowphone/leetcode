class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        ALICE = 0
        BOB = 1
        n = len(piles)

        @cache
        def play(turn: Literal[0, 1], index: int, M: int):
            max_scores = (0, 0)
            if index >= n:
                return max_scores
            
            for X in range(1, min(2 * M, n) + 1 ):
                earned = sum(piles[index:index+X])
                new_index = index + X

                
                candidate = play((turn + 1) % 2, new_index, max(M, X))

                new_scores = {
                    0: (candidate[0] + earned, candidate[1]),
                    1: (candidate[0], candidate[1] + earned),
                }[turn]
                max_scores = max(
                    max_scores,
                    new_scores,
                    key=lambda it: it[turn]
                )

            return max_scores

        return play(turn=0, index=0, M=1)[0]