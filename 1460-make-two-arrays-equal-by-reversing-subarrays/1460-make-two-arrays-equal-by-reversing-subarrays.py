from collections import Counter as multiset
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # By reversing two adjacent elements, we can swap two items
        # and at last we can sort the whole array. 
        return multiset(target) == multiset(arr)