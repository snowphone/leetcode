class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def get(idx):
            if idx < 0:
                return -987654321
            elif idx >= len(arr):
                return -987654321
            return arr[idx]

        b, e = 0, len(arr)
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