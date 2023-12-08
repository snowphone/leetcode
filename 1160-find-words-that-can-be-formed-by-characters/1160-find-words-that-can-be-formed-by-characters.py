from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        bigcnt = Counter(chars)
        def subset(small):
            smallcnt = Counter(small)
        
            for ch in smallcnt.keys():
                if smallcnt[ch] > bigcnt.get(ch, 0):
                    return False
            return True
        answer = 0

        for it in words:
            if subset(it):
                answer += len(it)

        return answer