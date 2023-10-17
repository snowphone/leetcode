class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        "Naive backtracking"
        def valid(s: str):
            stk = []
            for ch in s:
                if stk and (stk[-1], ch) == ('(', ')'):
                    stk.pop()
                else:
                    stk.append(ch)
            return not stk

        def fn(nchars: int):
            if nchars == 0:
                return ['']
            sub = fn(nchars - 1)

            answer = []
            for tmp in sub:
                answer += [
                    tmp + '(',
                    tmp + ')',
                ]
            return answer
        
        return [
            it for it in  fn(n * 2) if valid(it)
        ]