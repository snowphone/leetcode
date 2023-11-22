class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n_row = len(nums)

        tmp = []
        for i in range(n_row):
            line = nums[i]
            for j in range(len(line)):
                tmp.append( (i+j, -i, line[j]) )

        tmp.sort()

        return [it[-1] for it in tmp]