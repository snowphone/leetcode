from collections import Counter

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        close_yn = Counter(customers)
        open_yn = defaultdict(int)

        n = len(customers)
        penalty = lambda: open_yn['N'] + close_yn['Y']

        so_far_penalty = penalty()
        answer = 0

        for close_at in range(1, n+1):
            yn = customers[close_at - 1]
            close_yn[yn] -= 1
            open_yn[yn] += 1

            if penalty() < so_far_penalty:
                so_far_penalty = penalty()
                answer = close_at


        return answer
