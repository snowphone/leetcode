class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def fn(b: int, e: int):
            sz = e - b
            if sz <= 3:
                return next( (i for i in range(b, e) if nums[i] == target), -1 )
            
            m = (b + e) // 2
            if nums[b] < nums[m] < nums[e-1]:  # Fully sorted
                if nums[m] <= target:
                    return fn(m, e)
                return fn(b, m)
            elif nums[b] < nums[m] > nums[e-1]: # Top is at the rightside. Leftside is sorted
                if nums[b] <= target < nums[m]:
                    return fn(b, m)
                return fn(m, e)
            elif nums[b] > nums[m] < nums[e-1]: # Top is at the leftside. Rightside is sorted
                if nums[m] <= target <= nums[e-1]:
                    return fn(m, e)
                return fn(b, m)
            
            return -987654321
        
        return fn(0, len(nums))