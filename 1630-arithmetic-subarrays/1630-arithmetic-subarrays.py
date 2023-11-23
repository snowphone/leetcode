class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for fst, lst in zip(l, r):
            bag = set(nums[fst:lst+1])
            m, M = min(nums[fst:lst+1]), max(nums[fst:lst+1])
            diff = (M - m) / (lst - fst)
            
            answer.append(
                all(
                    m + i * diff in bag
                    for i in range(lst - fst + 1)
                )
            )
                
        return answer