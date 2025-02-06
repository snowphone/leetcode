class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prodmap = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                it, jt = nums[i], nums[j]
                if 0 in [it, jt]:
                    continue
                prodmap[it * jt].append((it, jt))

        answer = 0
        for pairlist in prodmap.values():
            sz = len(pairlist)
            answer += sz * (sz - 1) * 4
        return answer
