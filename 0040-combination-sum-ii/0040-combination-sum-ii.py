class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        @cache
        def fn(idx, target):
            if target < 0:
                return []
            if idx == len(candidates):
                return []

            me = candidates[idx]
            if target == me:
                return [ (me, ) ]
            
            answer = []

            for i in range(idx):
                subanswer = fn(i, target - me)

                for it in subanswer:
                    answer.append(tuple([*it, me]))

            return answer

        answer = set()
        for i in range(len(candidates)):
            answer |= set(fn(i, target))
        return list(answer)