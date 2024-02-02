class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        template = "123456789"
        low_len = len(str(low))
        high_len = len(str(high))
        answer = []
        for digit in range(low_len, high_len + 1):
            for i in range(10 - digit):
                numstr = template[i:i+digit]
                n = int(numstr)
                if not (low <= n <= high):
                    continue
                answer.append(n)
            
        return answer