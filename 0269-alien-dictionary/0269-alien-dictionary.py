from itertools import chain
from queue import SimpleQueue

class Solution:
    def analyze(self, lhs: str, rhs: str, graph, indegree):
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
        
        return len(lhs) <= len(rhs)
                
    def alienOrder(self, words: List[str]) -> str:
        # Topological sort
        graph = defaultdict(set)
        indegree = defaultdict(set)

        for ch in chain(*words):
            graph[ch]
            indegree[ch]

        if len(words) == 1:
            return ''.join(set(words[0]))

        for i, lhs in enumerate(words):
            for j in range(i+1, len(words)):
                rhs = words[j]
                if not self.analyze(lhs, rhs, graph, indegree):
                    return ''
        
        q = SimpleQueue()
        for ch in graph.keys():
            cnt = len(indegree[ch])
            if cnt != 0:
                continue
            q.put(ch)
        
        print(graph)
        print(indegree)
        
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
            return ''  # Cycle detected

        return ''.join(answer)


        


