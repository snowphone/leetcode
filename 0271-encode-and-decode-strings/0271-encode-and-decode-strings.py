class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        answer = []
        answer.append( str(len(strs) ).ljust(4, ' ') )

        for s in strs:
            answer.append( str(len(s) ).ljust(4, ' ') )
            answer.append(s)

        return ''.join(answer)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        n = int(s[:4])
        s = s[4:]

        answer = []
        for _ in range(n):
            sz = int(s[:4])
            s = s[4:]
            answer.append(s[:sz])
            s = s[sz:]
        return answer


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))