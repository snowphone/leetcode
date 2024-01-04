from collections import Counter
'''
1: x

2:       2
3:       3
4:       2+2
5:       2+3
6:       3+3
7:       3+2 +2

8:  3+3 +2
9:  3+3 +3
10: 3+3 +2+2
11: 3+3 +3+2
12: 3+3 +3+3
13: 3+3 +3+2+2
'''

class Solution:
    def ops(self, n: int):
        match (n-2) % 6 + 2:
            case 2|3:   return 1 + ((n-2) // 6) * 2
            case 4|5|6: return 2 + ((n-2) // 6) * 2
            case 7:     return 3 + ((n-2) // 6) * 2
        raise RuntimeError("Dead end")
    
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)

        answer = 0
        for cnt in counter.values():
            if cnt == 1:
                return -1
            answer += self.ops(cnt)

        return answer