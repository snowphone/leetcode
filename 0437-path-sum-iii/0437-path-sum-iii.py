# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        sum(nums[i+1, j+1]) == k
         <=> s(j) - s(i) == k, where def s(i): return sum(nums[0:i+1])
         <=> s(i) exists s.t. s(j) - k == s(i)
        

        """
        

        def dfs(root, acc, pfsum):
            answer = 0
            if not root:
                return answer

            acc += root.val  # Update s(j)
            si = acc - targetSum
            answer += pfsum[si]
            pfsum[acc] += 1

            for child in [root.left, root.right]:
                answer += dfs(child, acc, pfsum.copy())
            return answer
        
        cache = defaultdict(int)
        cache[0] = 1
        return dfs(root, 0, cache)