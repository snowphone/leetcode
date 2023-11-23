class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for fst, lst in zip(l, r):
            tmp = sorted( nums[fst:lst+1] )
            target = tmp[1] - tmp[0]

            answer.append(
                all( tmp[i] - tmp[i-1] == target for i in range(1, lst - fst + 1) )
            )
        return answer