from itertools import chain
from queue import SimpleQueue

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Topological sort

        if len(words) == 1:
            return ''.join(set(words[0]))

        graph = defaultdict(set)
        indegree = defaultdict(set)

        for ch in chain(*words):
            graph[ch]
            indegree[ch]

        for i, lhs in enumerate(words):
            for j in range(i+1, len(words)):
                rhs = words[j]
                if not self._analyze(lhs, rhs, graph, indegree):
                    return ''
        
        q = SimpleQueue()
        for ch in graph.keys():
            cnt = len(indegree[ch])
            if cnt != 0:
                continue
            q.put(ch)
        
        answer = []
        while not q.empty():
            ch = q.get()
            if ch in answer:
                continue
            answer.append(ch)

            for adj in graph[ch]:
                indegree[adj] -= { ch }
                if len(indegree[adj]) == 0:
                    q.put(adj)

        if any(it for it in indegree.values()):
            return ''  # Cycle between characters detected

        return ''.join(answer)

    def _analyze(
        self,
        lhs: str, rhs: str,
        graph: Dict[str, Set[str]], indegree: Dict[str, Set[str]]
    ):
        """
        Return true if no problem
        Otherwise, it is not sorted properly.
        """
        n = min(len(lhs), len(rhs))

        for i in range(n):
            it = lhs[i]
            jt = rhs[i]
            if it == jt:
                graph[it]
                continue
            graph[it].add(jt)
            indegree[jt].add(it)
            return True
        
        # If the prefix is same, the latter should be longer
        return len(lhs) <= len(rhs)
                

