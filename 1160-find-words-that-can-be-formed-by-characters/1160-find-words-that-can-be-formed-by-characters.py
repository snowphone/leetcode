from collections import Counter

def subset(big, small):
    bigcnt = Counter(big)
    smallcnt = Counter(small)

    for ch in smallcnt.keys():
        if smallcnt[ch] > bigcnt.get(ch, 0):
            return False
    return True

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        answer = 0

        for it in words:
            if subset(chars, it):
                answer += len(it)

        return answer