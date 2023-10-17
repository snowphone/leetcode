class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        graph = defaultdict(list)

        # Create a graph
        for i in range(n):
            if leftChild[i] != -1:
                graph[i].append(leftChild[i])
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                graph[i].append(rightChild[i])
                indegree[rightChild[i]] += 1
        
        roots = [ i for i, it in enumerate(indegree) if it == 0 ]
        if len(roots) != 1:
            return False  # Only one root is allowed
        root = roots[0]
        
        visited = set()

        def dfs(root):
            if root in visited:
                return False
            
            visited.add(root)
            
            return all(
                dfs(child) for child in graph[root]
            )
        
        # Visit only once but every node
        return dfs(root) and len(visited) == n