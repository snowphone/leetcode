class Solution:
    def largestOddNumber(self, num: str) -> str:

      idx = next((i for i in range(len(num)-1, -1, -1) if num[i] in "13579" ), -1)
      return num[:idx+1]
