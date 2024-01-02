from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)

        answer = []

        for n, cnt in c.items():
            while len(answer) < cnt:
                answer.append([])
            for i in range(cnt):
                answer[i].append(n)
        return answer
        