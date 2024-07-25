class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        m = n // 2 

        lhs = self.sortArray(nums[:m])
        rhs = self.sortArray(nums[m:])

        answer = []
        i, j = 0, 0
        while i < len(lhs) or j < len(rhs):
            if i == len(lhs):
                answer += rhs[j:]
                j = len(rhs)
            elif j == len(rhs):
                answer += lhs[i:]
                i = len(lhs)
            elif lhs[i] < rhs[j]:
                answer.append(lhs[i])
                i += 1
            else:
                answer.append(rhs[j])
                j += 1
        return answer
        
        