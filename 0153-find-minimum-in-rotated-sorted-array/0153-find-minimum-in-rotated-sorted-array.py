class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def fn(b: int, e: int):
            "Find an index with the biggest element"
            if e - b <= 3:
                return max(range(b, e), key=nums.__getitem__)
            
            m = (b + e) // 2
            
            return {
                nums[b] > nums[m] < nums[e-1]: (  # Hill is on the left side.
                    lambda: fn(b, m)
                ),
                nums[b] < nums[m] > nums[e-1]: (  # Hill is on the right side.
                    lambda: fn(m, e)
                ),
                nums[b] < nums[m] < nums[e-1]: (  # All sorted
                    lambda: e-1
                ),
            }[True]()
            
        
        n = len(nums)
        idx = fn(0, n)
        return nums[(idx + 1) % n]