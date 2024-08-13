class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        def fn(idx, target):
            if target < 0:
                return []
            if target == 0:
                return [ [] ]
            if idx == n:
                return []

            me = candidates[idx]

            ans = []

            for it in fn(idx+1, target - me): # Use myself
                it.append(me)
                ans.append(it)

            next_idx = next((i for i in range(idx+1, n) if candidates[i] != candidates[idx]), n)    
            for it in fn(next_idx, target):  # Not use myself
                ans.append(it)

            return ans

        return fn(0, target)