class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def fn(b: int, e: int):
            "Find an index with the biggest element"
            if e - b <= 3:
                return max(range(b, e), key=nums.__getitem__)
            
            m = (b + e) // 2
            
            if nums[b] > nums[m] < nums[e-1]:  # Hill is on the left side.
                return fn(b, m)
            elif nums[b] < nums[m] > nums[e-1]: # Hill is on the right side.
                return fn(m, e)
            elif nums[b] < nums[m] < nums[e-1]: # All sorted
                return e-1
            
            raise RuntimeError("Dead end")
                
                
            return
        
        n = len(nums)
        idx = fn(0, n)
        return nums[(idx + 1) % n]