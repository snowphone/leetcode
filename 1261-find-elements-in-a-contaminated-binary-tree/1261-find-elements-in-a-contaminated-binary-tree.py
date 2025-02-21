# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.numset = set()
        self._recover(self.root, 0)

    def find(self, target: int) -> bool:
        return target in self.numset
    
    def _recover(self, root: TreeNode, fixed_value: int):
        self.numset.add(fixed_value)
        root.val = fixed_value
        root.left and self._recover(root.left, root.val * 2 + 1)
        root.right and self._recover(root.right, root.val * 2 + 2)
        return
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)