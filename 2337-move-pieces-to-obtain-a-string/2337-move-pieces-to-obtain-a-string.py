from collections import Counter


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        def convert(s: str):
            return [(i, ch) for i, ch in enumerate(s) if ch in "LR"]

        start_list = convert(start)
        target_list = convert(target)
        
        if len(start_list) != len(target_list):
            return False

        for (sidx, sch), (tidx, tch) in zip(start_list, target_list):
            if sch != tch:
                return False
            if sch == 'L' and not (tidx <= sidx):
                return False
            if sch == 'R' and not (sidx <= tidx):
                return False
        return True
