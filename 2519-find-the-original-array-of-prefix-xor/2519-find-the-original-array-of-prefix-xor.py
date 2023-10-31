class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        answer= pref[:1]

        for i in range(1, len(pref)):
            answer.append(pref[i] ^ pref[i-1])
        return answer