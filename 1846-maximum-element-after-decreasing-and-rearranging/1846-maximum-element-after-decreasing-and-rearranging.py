class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        sz = len(arr)
        arr.sort()

        for i, it in enumerate(arr, 1):
            if i <= it:
                continue  # Able to decrease the number
            # i > it
            if it == arr[-1]:
                return it
            return it + 1

        return sz
