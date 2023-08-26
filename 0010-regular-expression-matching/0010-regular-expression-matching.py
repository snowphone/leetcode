import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        compact = re.sub(r"\*+", '*', p)
        return re.match(f"^{compact}$", s)