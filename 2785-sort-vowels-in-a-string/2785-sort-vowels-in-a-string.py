class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [ch for ch in s if ch.lower() in 'aeiou']
        vowels.sort()

        idx = 0
        
        answer = list(s)
        
        for i, ch in enumerate(answer):
            if ch.lower() not in 'aeiou':
                continue
            answer[i] = vowels[idx]
            idx += 1
        return ''.join(answer)
        