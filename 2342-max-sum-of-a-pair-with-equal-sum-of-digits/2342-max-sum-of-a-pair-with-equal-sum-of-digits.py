class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def ds(i: int):
            return sum(
                int(digit)
                for digit in str(i)
            )
        
        digit_sums = [ds(it) for it in nums]
        acc_to_num = defaultdict(list)

        for i, acc in enumerate(digit_sums):
            acc_to_num[acc].append(nums[i])
        
        answer = -1
        for num_list in acc_to_num.values():
            if len(num_list) < 2:
                continue
            answer = max(
                answer,
                sum( sorted(num_list)[-2:] ),
            )
        return answer

        