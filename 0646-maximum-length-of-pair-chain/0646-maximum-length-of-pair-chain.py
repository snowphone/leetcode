from operator import itemgetter
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=itemgetter(1))

        ans = pairs[:1]

        for b, e in pairs[1:]:
            if ans[-1][1] < b:
                ans.append((b, e))

        return len(ans)