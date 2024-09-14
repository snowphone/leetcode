class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        chunks = self._make_chunks(nums)
        m = max(chunks, key=lambda it: it[0])[0]
        return max((it for it in chunks if it[0] == m), key=lambda it: it[1])[1]

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