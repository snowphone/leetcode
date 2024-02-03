class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        @cache
        def fn(i: int):
            """
            Return an answer for range of [0,i] indices.
            """
            if i == 0: return arr[0] if k else 0

            answer = 0
            sz = i+1
            for kk in range(1, min(sz, k)+1):
                answer = max(
                    answer,
                    fn(i-kk) + max(arr[sz-kk:sz]) * kk,
                )
            return answer

        return fn(len(arr) - 1)