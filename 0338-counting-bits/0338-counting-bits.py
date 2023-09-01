class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0]
        while len(answer) < (n+1):
            answer.extend([
                it + 1 for it in answer
            ])
        return answer[:n+1]