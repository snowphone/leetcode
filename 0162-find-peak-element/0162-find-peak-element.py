class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def get(idx):
            if idx < 0:
                return -987654321
            elif idx >= len(nums):
                return -987654321
            return nums[idx]

        b, e = 0, len(nums)
        while b < e:
            m_idx = (b + e) // 2
            prev, me, nxt = get(m_idx - 1), get(m_idx), get(m_idx + 1)
            if prev < me > nxt:
                return m_idx
            elif prev < me < nxt:
                b, e = m_idx + 1, e
            else:
                b, e = b, m_idx
        return m_idx 