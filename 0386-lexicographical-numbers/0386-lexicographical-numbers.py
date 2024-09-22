class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return list(self._solve(n))

    def _solve(self, n: int):
        for i in range(1, 10):
            if i <= n:
                yield i
                yield from self._generate(str(i), n)

    def _generate(self, prefix: str, limit: int):
        for i in range(0, 10):
            candidate = f"{prefix}{i}"
            candidate_num = int(candidate)
            if candidate_num <= limit:
                yield candidate_num
                yield from self._generate(candidate, limit)
        return