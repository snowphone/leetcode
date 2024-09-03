class Solution:
    def _conv(self, ch: str):
        return ord(ch) - ord('a') + 1

    def getLucky(self, s: str, k: int) -> int:
        num_list = map(self._conv, s)
        digitsum =  ''.join(map(str, num_list))
        
        for _ in range(k):
            digitsum = str(sum(int(it) for it in digitsum))
        return int(digitsum)
        