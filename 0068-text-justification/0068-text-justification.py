class Solution:
    def cut(self, words, maxWidth):
        page = []
        line = []
        sz = lambda: sum((len(it) for it in line) ) + (len(line) - 1 if line else 0)
        n = len(words)
        i = 0
        while i < n:
            word = words[i]
            line.append(word)
            if sz() > maxWidth:
                line.pop()
                page.append(line.copy())
                line = []
            else:
                i += 1
        if line:
            page.append(line.copy())
        return page
    
    def justify(self, line, maxWidth):
        n = len(line)
        
        nleft = maxWidth - sum(map(len, line))
        nspaces = len(line) - 1 if line else 0
        
        answer = []
        for i in range(n-1):
            word = line[i]
            pad = ceil( nleft / nspaces )
            answer += [ word, ' ' * pad ]

            nspaces -= 1
            nleft -= pad

        if answer:
            answer += [' ' * nleft, line[-1]]
        else:
            answer = [ line[-1].ljust(maxWidth) ]

        return ''.join(answer)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        page = self.cut(words, maxWidth)

        return [
            *(self.justify(it, maxWidth) for it in page[:-1]),
            " ".join(page[-1]).ljust(maxWidth),
        ] 