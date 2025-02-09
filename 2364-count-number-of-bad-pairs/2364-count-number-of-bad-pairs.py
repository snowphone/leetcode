class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        mapping = defaultdict(int)

        for i, it in enumerate(nums):
            mapping[it - i] += 1
        
        answer = 0

        n = len(nums)
        for cnt in mapping.values():
            others = n - cnt
            answer += cnt * others

        return answer // 2

