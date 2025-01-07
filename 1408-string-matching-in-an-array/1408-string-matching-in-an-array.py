class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        for i, word in enumerate(words):
            for j, tmp in enumerate(words):
                if i == j:
                    continue
                if word not in tmp:
                    continue
                answer.append(word)
                break
        return answer