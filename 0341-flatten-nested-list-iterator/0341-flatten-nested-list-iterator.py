# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


import itertools
from typing import List

def gen(nestedList: List[NestedInteger]):
    for it in nestedList:
        if it.isInteger():
            yield it.getInteger()
        else:
            sublist = it.getList()
            yield from gen(sublist)


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.gen = gen(nestedList)
        self.sentinel = object()
        
    def next(self) -> int:
        return next(self.gen)
    
    def hasNext(self) -> bool:
        try:
            tmp = next(self.gen)
            self.gen = itertools.chain([tmp], self.gen)
            return True
        except StopIteration:
            return False