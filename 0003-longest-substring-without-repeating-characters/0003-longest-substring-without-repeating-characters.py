class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        l = 0
        answer = 0

        def repeating_chars():
            return ch in index_map and index_map[ch] >= l

        for r, ch in enumerate(s):
            if repeating_chars():
                idx = index_map[ch]
                l = idx + 1
            index_map[ch] = r
            answer = max(answer, r - l + 1)
        return answer
