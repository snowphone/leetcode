class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        rhs = [0, 0]
        for ch in s:
            rhs[ord(ch) - ord('a')] += 1
        lhs = [0, 0]

        answer = 987654321

        # Goal: 
        #   s[:i] == 'a' * i
        #   s[i:] == 'b' * (n - i)
        for i in range(n+1):
            answer = min(
                answer,
                lhs[1] + rhs[0],
            )
            if i < n:
                ch = s[i]
                lhs[ord(ch) - ord('a')] += 1
                rhs[ord(ch) - ord('a')] -= 1
        return answer