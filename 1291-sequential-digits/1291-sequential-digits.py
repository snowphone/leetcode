class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        template = "123456789"
        low_len = len(str(low))
        high_len = len(str(high))
        return [ it 
            for digit in range(low_len, high_len + 1)
            for i in range(10 - digit)
            if low <= (it := int( template[i:i+digit] ) ) <= high
        ]