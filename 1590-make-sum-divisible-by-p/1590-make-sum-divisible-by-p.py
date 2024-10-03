class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        whole = sum(nums) % p
        if whole == 0:
            return 0

        # Goal: (whole - sum[i..j]) % p == 0
        #        whole % p == sum[i..j] % p
        #        whole % p == pm[j] % p - pm[i-1] % p
        # 
        #            whole == it - target
        #           target == it - whole
        #        target = sum[0..i-1]

        prefix_mod = nums[:1]  # sum[0..i]
        prefix_mod[0] %= p
        for it in nums[1:]:
            prefix_mod.append( (prefix_mod[-1] + it) % p )
        
        answer = len(nums)
        mapping = {0: -1}

        for j, it in enumerate(prefix_mod):
            target = (it - whole + p) % p 
            i = mapping.get(target)
            if i is not None:
                answer = min(
                    answer,
                    (j - i),
                )
            mapping[it] = j
        return answer if answer != len(nums) else -1
