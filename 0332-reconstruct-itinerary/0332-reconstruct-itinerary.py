from queue import SimpleQueue
from sortedcontainers import SortedList

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(SortedList)

        for f, t in tickets:
            graph[f].add(t)

        def dfs(frm, graph, n_node):
            if not n_node:
                return True, [frm]

            for it in graph[frm]:
                graph[frm].remove(it)
                ok, ans = dfs(it, graph, n_node - 1)
                if ok:
                    graph[frm].add(it)
                    return True, [frm, *ans]
                graph[frm].add(it)
            return False, []
        
        ok, answer = dfs("JFK", graph, sum(len(it) for it in graph.values()) )
        return answer