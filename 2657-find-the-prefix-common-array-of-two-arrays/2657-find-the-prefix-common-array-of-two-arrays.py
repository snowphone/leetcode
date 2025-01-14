class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        n = len(a)
        answer = []
        lhs = set()
        rhs = set()

        prev = 0
        for l, r in zip(a, b):
            lhs.add(l)
            rhs.add(r)

            if (common := (lhs & rhs)):
                answer.append(prev + len(common))
                lhs -= common
                rhs -= common
            else:
                answer.append(prev)
            prev = answer[-1]

        return answer