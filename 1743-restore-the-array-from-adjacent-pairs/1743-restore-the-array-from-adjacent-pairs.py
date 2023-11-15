class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        links = defaultdict(list)
        for i, j in adjacentPairs:
            links[i].append(j)
            links[j].append(i)
        start = next(i for i, j in links.items() if len(j) == 1)

        answer = [start]
        prev = None
        it = start
        while True:
            adj = next( (jt for jt in links[it] if jt not in [None, prev] ), None )
            if adj == None:
                break
            answer.append(adj)
            it, prev = adj, it
        return answer