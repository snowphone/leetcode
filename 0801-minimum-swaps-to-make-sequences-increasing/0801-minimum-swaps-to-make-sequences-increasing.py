class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        def get(idx: int, swapped: Literal[0, 1]):
            if swapped:
                return nums2[idx], nums1[idx]
            return nums1[idx], nums2[idx]

        @cache
        def solve(idx: int, swapped: Literal[0, 1]):
            if idx == 0:
                return swapped
            
            i, j = get(idx, swapped)

            answer = 10 ** 5 + 7
            for prev_swapped in [False, True]:
                prev_i, prev_j = get(idx-1, prev_swapped)
                if prev_i < i and prev_j < j:
                    answer = min( answer, solve(idx-1, prev_swapped) + swapped )
            return answer

        for i in range(n):  # Warm-up cache
            solve(i, 0); solve(i, 1)
        
        return min(solve(n-1, 0), solve(n-1, 1))