class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numset = frozenset(nums)

        sz = len(nums[0])

        def find(s: str, i: int):
            if i == sz:
                return s if s not in numset else None
            
            return find('0' + s, i+1) or find('1'+s, i+1)
        
        return find('', 0)