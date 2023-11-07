class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def fn(word):
           if len(word) == 1:
               return [ "1", word ]
           
           answer = []
           for it in fn(word[1:]):
               answer += [f"{word[0]}{it}", f"1{it}"]
           return answer 

        def merge(word):
            stk = []
            for ch in word:
                if ch != '1':
                    stk.append(ch)
                elif not stk:
                    stk.append(1)
                elif isinstance(stk[-1], int):
                    stk[-1] += 1
                else:
                    stk.append(1)
            return ''.join(str(it) for it in stk)
         

        return set(merge(it) for it in fn(word))