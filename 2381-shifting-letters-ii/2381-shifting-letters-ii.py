class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        delta = [0 for _ in s]

        def tochr(i: int):
            base = ord("a")
            return chr(((i - base) + 26) % 26 + base)

        for l, r, direction in shifts:
            step = 1 if direction == 1 else -1

            delta[l] += step
            if r + 1 < len(delta):
                delta[r + 1] -= step

        for i in range(1, len(delta)):
            delta[i] += delta[i - 1]

        return "".join(tochr(ord(ch) + delta[i]) for i, ch in enumerate(s))
