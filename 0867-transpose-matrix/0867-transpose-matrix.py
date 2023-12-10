class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        return [
            list(it) for it in zip(*matrix)
        ]