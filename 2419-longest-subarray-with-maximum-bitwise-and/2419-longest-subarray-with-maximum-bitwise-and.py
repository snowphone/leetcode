class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        chunks = self._make_chunks(nums)
        maxima, maxima_cnt = 0, 0
        print(chunks)
        for k, cnt in chunks:
            if k > maxima:
                maxima, maxima_cnt = k, cnt
            elif k == maxima:
                maxima_cnt = max(cnt, maxima_cnt)
        return maxima_cnt

    def _make_chunks(self, nums: list[int]):
        answer = []
        last, cnt = nums[0], 1
        for it in nums[1:]:
            if last == it:
                cnt += 1
            else:
                answer.append((last, cnt))
                last, cnt = it, 1
        answer.append((last, cnt))
        
        return answer