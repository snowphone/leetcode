class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        @cache
        def fn(i: int):
            if i < 0:  return 0
            if i == 0: return arr[0] if k else 0

            answer = 0
            for kk in range(1, min(i+1, k)+1):
                answer = max(
                    answer,
                    fn(i-kk) + max(arr[i-kk+1:i+1]) * kk,
                )
            return answer

        return fn(len(arr) - 1)