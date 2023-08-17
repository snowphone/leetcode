from queue import SimpleQueue

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for t, f in prerequisites:
            graph[f].append(t)
            indegree[t] += 1
        
        remaining = set(range(numCourses))
        q = SimpleQueue()
        for nd in range(numCourses):
            cnt = indegree[nd]
            if cnt == 0:
                q.put(nd)
                
        
        while not q.empty():
            nd = q.get()
            remaining.remove(nd)

            for nxt in graph[nd]:
                indegree[nxt] -= 1
                if nxt in remaining and indegree[nxt] == 0:
                    q.put(nxt)
            
        return not remaining
