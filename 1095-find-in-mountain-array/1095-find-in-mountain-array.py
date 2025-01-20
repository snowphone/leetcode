# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountainArr: "MountainArray") -> int:
        peek_idx = self.find_peek(target, mountainArr)

        if (i := self.bsearch(mountainArr, target, 0, peek_idx + 1)) > -1:
            return i
        return self.bsearch(
            mountainArr, -target, peek_idx, mountainArr.length(), key=lambda it: -it
        )

    def find_peek(self, target: int, mountainArr: "MountainArray"):
        def get(idx):
            if idx < 0:
                return -987654321
            elif idx >= mountainArr.length():
                return -987654321
            return mountainArr.get(idx)

        b, e = 0, mountainArr.length()
        while b < e:
            mid = (b + e) // 2
            prev, me, nxt = get(mid - 1), get(mid), get(mid + 1)
            if prev < me > nxt:
                return mid
            elif prev < me < nxt:
                b, e = mid + 1, e
            else:
                b, e = b, mid
        return mid

    def bsearch(
        self,
        arr: "MountainArray",
        target: int,
        b: int,
        e: int,
        key=lambda it: it,
    ):
        while b < e:
            mid = (b + e) // 2
            mid_it = key(arr.get(mid))
            if mid_it == target:
                return mid
            elif mid_it < target:
                b, e = mid + 1, e
            else:
                b, e = b, mid
        return -1
