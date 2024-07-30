from collections import Counter
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        rhs = Counter(s)
        lhs = {'a': 0, 'b': 0}

        answer = 987654321

        # Goal: 
        #   s[:i] == 'a' * i
        #   s[i:] == 'b' * (n - i)
        for i in range(n+1):
            answer = min(
                answer,
                lhs['b'] + rhs['a'],
            )
            if i < n:
                ch = s[i]
                lhs[ch] += 1
                rhs[ch] -= 1
        return answer