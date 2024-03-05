class Solution:
    def minimumLength(self, s: str) -> int:
        group = self.group_by_adjacency(s)
        n = len(group)

        i = 0
        j = n-1
        while i < j:
            if group[i][0] == group[j][0]:
                i+=1
                j-=1
                continue
            else:
                break

        if i < j: 
            return sum(i for ch, i in group[i:j+1])
        elif group[i][1] > 1:
            return 0
        else:
            return 1
    
    def group_by_adjacency(self, s: str):
        answer = []
        i = 0
        n = len(s)
        while i < n:
            ch = s[i]
            j = next((k for k in range(i+1, n) if s[k] != ch), n)
            answer.append( (ch, j-i) )
            i = j
        return answer