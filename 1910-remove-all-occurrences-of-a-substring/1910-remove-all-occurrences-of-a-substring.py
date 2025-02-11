class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        sz = len(s)
        part_sz = len(part)

        def match():
            if len(stk) < part_sz:
                return False
            return all( stk[-i] == part[-i] for i in range(1, part_sz + 1) )

        stk = ['']
        for i, ch in enumerate(s):
            stk.append(ch)

            if stk[-1] == part[-1] and match():
                del stk[-part_sz:]  # pop

        
            
        return ''.join(stk)

            