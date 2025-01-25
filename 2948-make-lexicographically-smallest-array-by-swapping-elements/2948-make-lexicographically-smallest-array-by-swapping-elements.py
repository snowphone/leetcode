from collections import deque


class Solution:

    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> List[int]:
        groups = self._get_groups(nums, limit)
        num_to_group = {it: group for group in groups for it in group}

        sz = len(nums)
        for i in range(0, sz):
            it = nums[i]
            group = num_to_group[it]
            nums[i] = group.popleft()

        return nums

    def _get_groups(self, nums: list[int], limit: int):
        n = len(nums)
        s = sorted(nums)
        groups = [deque(s[:1])]
        sz = len(nums)
        for i in range(1, sz):
            it = s[i]
            if it - groups[-1][-1] <= limit:
                groups[-1].append(it)
            else:
                groups.append(deque([it]))
        return groups
