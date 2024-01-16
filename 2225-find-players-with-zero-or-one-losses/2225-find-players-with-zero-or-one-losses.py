class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        users = set()
        for w, l in matches:
            users |= {w, l}

        loses = {u: 0 for u in users}
        for w, l in matches:
            loses[l] += 1
        
        answer = [[], []]
        for u in sorted(users):
            if not loses[u]:
                answer[0].append(u)
            if loses[u] == 1:
                answer[1].append(u)
        return answer