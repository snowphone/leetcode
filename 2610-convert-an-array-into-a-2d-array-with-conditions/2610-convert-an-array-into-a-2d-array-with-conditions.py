from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)

        answer = [ [] for _ in range(max(c.values()))]

        for n, cnt in c.items():
            for i in range(cnt):
                answer[i].append(n)
        return answer
        