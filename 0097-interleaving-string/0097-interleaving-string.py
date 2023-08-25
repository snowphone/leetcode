class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def fn(i, j, k):
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            if k == len(s3):
                return False

            if s1[i] == s3[k] and s2[j] == s3[k]:
                return fn(i+1, j, k+1) or fn(i, j+1, k+1)
            if s1[i] == s3[k]:
                return fn(i+1, j, k+1)
            if s2[j] == s3[k]:
                return fn(i, j+1, k+1)
            return False

        return fn(0, 0, 0)
            
