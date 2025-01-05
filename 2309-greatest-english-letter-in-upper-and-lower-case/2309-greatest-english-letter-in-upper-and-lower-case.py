class Solution:
    def greatestLetter(self, s: str) -> str:
        chars = set(s)

        return next(
            (
                ch
                for i in range(ord("Z"), ord("A") - 1, -1)
                if (ch := chr(i)) in chars and ch.lower() in chars
            ),
            "",
        )
