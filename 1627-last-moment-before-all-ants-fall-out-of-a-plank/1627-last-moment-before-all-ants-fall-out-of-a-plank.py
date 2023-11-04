class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        """
        Actually, I don't have to differenciate each ant, so I cannot tell
        1) ants meet and change others from 2) ants meet and go the same direction.
        """

        answer = []
        if left:
            answer.append(  max(left) )
        if right:
            answer.append(  n - min(right)  )
        return max(answer)