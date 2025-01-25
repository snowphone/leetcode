from sortedcontainers import SortedList
from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        s = sorted(nums)
        groups = [ deque(s[:1]) ]
        for it in s[1:]:
            if it - groups[-1][-1] <= limit:
                groups[-1].append(it)
            else:
                groups.append( deque([it] ) )
        
        num_to_group = {
            it: group
            for group in groups
            for it in group
        }

        sz = len(nums)
        for i in range(0, sz):
            it = nums[i]
            group = num_to_group[it]

            new_it = group.popleft()
            new_it_idx = nums.index(new_it, i)
            nums[i], nums[new_it_idx] = new_it, it

        return nums