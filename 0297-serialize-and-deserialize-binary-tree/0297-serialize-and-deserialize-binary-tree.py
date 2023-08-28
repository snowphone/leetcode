import re
from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


r"""
<Expr>     ::= <NodeExpr> | <NoneExpr>
<NodeExpr> ::= 'TreeNode' '(' <ValExpr> ',' <Expr> ',' <Expr> ')'
<ValExpr>  ::= '-'? \d+
<NoneExpr> ::= 'None'
"""


class IExpr:
    def __init__(self, tokens: deque[str]) -> None:
        self.tokens = tokens
        return

    def eval(self) -> TreeNode | None | int:
        ...


class Expr(IExpr):
    def eval(self) -> TreeNode | None:
        token = self.tokens[0]
        return {
            token == "TreeNode": lambda: TreeNodeExpr(self.tokens).eval(),
            token == "None": lambda: NoneExpr(self.tokens).eval(),
        }[True]()


class NoneExpr(IExpr):
    def eval(self) -> None:
        self.tokens.popleft()
        return None


class TreeNodeExpr(IExpr):
    def eval(self) -> TreeNode:
        self.tokens.popleft()  # TreeNode
        self.tokens.popleft()  # (
        val = ValExpr(self.tokens).eval()
        self.tokens.popleft()  # ,
        lhs = Expr(self.tokens).eval()
        self.tokens.popleft()  # ,
        rhs = Expr(self.tokens).eval()
        self.tokens.popleft()  # )

        tree = TreeNode(val)
        tree.left = lhs
        tree.right = rhs

        return tree


class ValExpr(IExpr):
    def eval(self) -> int:
        if self.tokens[0] == "-":
            self.tokens.popleft()
            return -int(self.tokens.popleft())
        return int(self.tokens.popleft())


class Codec:
    pattern = re.compile(r"None|TreeNode|[(),-]|\d+")

    def serialize(self, root: TreeNode | None) -> str:
        "Encodes a tree to a single string."
        if not root:
            return "None"
        return f"TreeNode({root.val}, {self.serialize(root.left)}, {self.serialize(root.right)})"

    def deserialize(self, data: str) -> TreeNode | None:
        "Decodes your encoded data to tree."

        tokens = deque(it.group() for it in self.pattern.finditer(data))

        return Expr(tokens).eval()