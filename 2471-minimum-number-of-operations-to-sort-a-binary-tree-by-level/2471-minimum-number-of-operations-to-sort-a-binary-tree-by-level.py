# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = self._bfs(root)
        answer = 0
        for lv in levels:
            answer += self.get_cnt_to_be_sorted(lv)
        return answer

    def get_cnt_to_be_sorted(self, arr):
        cnt = 0
        targets = sorted(arr)
        loc = {it: i for i, it in enumerate(arr)}
        n = len(arr)
        for i in range(n - 1):
            target = targets[i]
            j = loc[target]
            if i == j:
                continue
            arr[i], arr[j] = arr[j], arr[i]
            loc[arr[i]], loc[arr[j]] = i, j
            cnt += 1
        return cnt

    def _bfs(self, root):
        ans = []
        q = [root]
        while q:
            ans.append([it.val for it in q])
            new_q = []
            for it in q:
                if it.left:
                    new_q.append(it.left)
                if it.right:
                    new_q.append(it.right)
            q = new_q
        return ans
