class Solution:
    def compressedString(self, word: str) -> str:
        compressed = []
        self.solve(word, 0, compressed)
        return ''.join(compressed)
    
    def solve(self, word: str, idx: int, compressed: list[str]):
        sz = len(word)
        if idx >= sz:
            return
        ch = word[idx]
        def diff(ch, start):
            for i in range(start, start+9):
                if i >= sz:
                    return sz
                if word[i] != ch:
                    return i
            return start + 9
        end_idx = diff(ch, idx)
        compressed.append(
            f"{end_idx - idx}{ch}"
        )
        self.solve(word, end_idx, compressed)
        