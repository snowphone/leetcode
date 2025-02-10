class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        mapping = {}
        rev_mapping = {}
        for token, word in zip(pattern, words):
            mapping.setdefault(token, word)
            rev_mapping.setdefault(word, token)

            if mapping[token] != word:
                return False
            if rev_mapping[word] != token:
                return False
            
        return True