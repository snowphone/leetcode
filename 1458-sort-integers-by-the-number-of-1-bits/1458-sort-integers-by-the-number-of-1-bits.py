def sorter(n: int):
    count = 0
    for i in range(32):
        if n & (1 << i):
            count += 1
    return count, n

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        return sorted(arr, key=sorter)
        