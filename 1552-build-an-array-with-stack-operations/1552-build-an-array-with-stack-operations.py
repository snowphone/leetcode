class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        nums = list(range(n, 0, -1))

        for target_num in target:
            while target_num != nums[-1]:
                answer += ["Push", "Pop"]
                nums.pop()
            answer += ["Push"]
            nums.pop()
        return answer
            