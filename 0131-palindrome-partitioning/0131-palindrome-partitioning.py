class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n == 1:
            return [[s]]

        answer = []
        if s == s[::-1]:
            answer.append([s])
            
        for i in range(1, n):
            head, tail = s[:i], s[i:]
            if head != head[::-1]:
                continue
            subanswer = self.partition(tail)
            answer += [
                [head, *sub] for sub in subanswer
            ]
        return answer