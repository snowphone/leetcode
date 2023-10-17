"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        def nodes(node, mapping):
            if not node.neighbors:
                return mapping
            
            for it in node.neighbors:
                if it.val in mapping:
                    continue
                mapping[it.val] = it
                nodes(it, mapping)
            return mapping

        old = nodes(node, {node.val: node})
        new = { n: Node(n) for n, nd in old.items() }
        for i in old.keys():
            src = old[i]
            dst = new[i]
            if not src.neighbors:
                continue
            dst.neighbors = [
                new[adj.val] for adj in src.neighbors
            ]
        return new[node.val]


