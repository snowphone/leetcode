class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 0
        left = 0
        counter = defaultdict(int)

        for right in range(len(s)):
            ch = s[right]
            counter[ch] += 1
            while sum(counter.values()) - max(counter.values()) > k:
                ch2 = s[left]
                counter[ch2] -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer