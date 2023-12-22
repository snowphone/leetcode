class Solution:
    def maxScore(self, s: str) -> int:
        zeroes = s[:1].count('0')
        ones = s[1:].count('1')

        n = len(s)

        answer = zeroes + ones

        # partition between i and i+1
        for i in range(1, n-1):
            if s[i] == '0':
                zeroes += 1
            else:
                ones -= 1
            answer = max(answer, zeroes + ones)
        return answer