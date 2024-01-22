class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        m = len(nums)
        cnt = [0] * (m+1)
        for it in nums:
            cnt[it] += 1
        
        answer = [None, None]
        for i, it in enumerate(cnt):
            if i == 0:
                continue
            if it == 2:
                answer[0] = i
            if it == 0:
                answer[1] = i
                
        return answer