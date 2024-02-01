class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        answer = []
        n = len(nums)

        for i in range(0, n, 3):
            subarr = nums[i:i+3]
            if subarr[2] - subarr[0] > k :
                return []
            answer.append(subarr)
        
        return answer