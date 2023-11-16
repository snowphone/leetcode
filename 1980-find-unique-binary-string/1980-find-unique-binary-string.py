class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        numset = {int(it, 2) for it in nums}
        
        
        def tobin(num):
            answer = []
            for i in range(n):
                if num & (1 << i):
                    answer.append('1')
                else:
                    answer.append('0')
            return ''.join(reversed(answer))
        
        ans = next(i for i in range(2 ** n) if i not in numset)
        return tobin(ans)