from itertools import zip_longest

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        def convert(s: str):
            return ((i, ch) for i, ch in enumerate(s) if ch in "LR")

        start_list = convert(start)
        target_list = convert(target)

        for it in zip_longest(start_list, target_list):
            match it:
                case (None, _) | (_, None):
                    return False
                case ( (sidx, sch), (tidx, tch) ):
                    if (
                        (sch != tch) or
                        (sch == 'L' and not (tidx <= sidx) ) or
                        (sch == 'R' and not (sidx <= tidx) )
                    ):
                        return False
        return True
