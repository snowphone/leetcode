# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        MountainArray.__getitem__ = mountain_arr.get
        MountainArray.__len__ = mountain_arr.length

        def find(b: int, e: int):
            if e - b <= 3:
                return max(range(b, e), key=mountain_arr.get)
            
            m = (b + e) // 2
            
            i, j, k = mountain_arr[m-1], mountain_arr[m], mountain_arr[m+1]
            
            if i < j > k:
                return m
            elif i < j < k:
                return find(m, e)
            elif i > j > k:
                return find(b, m)
            
        def bsearch(b: int, e: int, target: int):
            if e - b <= 3:
                return next( (i for i in range(b, e) if mountain_arr[i] == target), -1)
            
            m = (b+e) // 2
            mit = mountain_arr[m]
            if mit < target:
                return bsearch(m, e, target)
            elif target < mit:
                return bsearch(b, m, target)
            return m
            
        n = len(mountain_arr)
        idx = find(0, n)  # peak idx

        i = bsearch(0, idx + 1, target)
        if 0 <= i <= idx and mountain_arr[i] == target:
            return i
        j = bsearch(idx+1, n, target)
        if idx < j < n and mountain_arr[j] == target:
            return j
        return -1