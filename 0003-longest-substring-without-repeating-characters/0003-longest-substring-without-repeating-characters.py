class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        bag = set()
        answer = 0
        for right, ch in enumerate(s):
            if ch in bag:
                while left < right:
                    ch2 = s[left]
                    bag.remove(s[left])
                    left += 1
                    if ch2 == ch:
                        break
            bag.add(ch)
            answer = max(answer, len(bag))
        return answer
