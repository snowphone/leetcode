import re

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pattern = '^.*' + '.*'.join(s) + '.*$'

        return re.match(pattern, t)

        