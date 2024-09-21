class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        answer = []

        for i in range(1, 10):
            if i <= n:
                answer.append(i)
                self._generate(str(i), n, answer)
        return answer
    
    def _generate(self, prefix: str, limit: int, answer: list[int]):
        for i in range(0, 10):
            candidate = f"{prefix}{i}"
            candidate_num = int(candidate)
            if candidate_num <= limit:
                answer.append(candidate_num)
                self._generate(candidate, limit, answer)
        return