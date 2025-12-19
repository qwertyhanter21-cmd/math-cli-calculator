from typing import List
from .expression_tree import TreeNode


class ExpressionParser:
    """Парсер математичних виразів у дерево."""

    def tokenize(self, expr: str) -> List[str]:
        tokens = []
        num = ""
        for ch in expr:
            if ch.isdigit() or ch == ".":
                num += ch
            else:
                if num:
                    tokens.append(num)
                    num = ""
                if ch.strip():
                    tokens.append(ch)
        if num:
            tokens.append(num)
        return tokens

    def to_rpn(self, tokens: List[str]) -> List[str]:
        """Алгоритм сортувальної станції (RPN)."""
        out, stack = [], []
        prec = {"+": 1, "-": 1, "*": 2, "/": 2}
        for t in tokens:
            if t.isdigit() or self._is_float(t):
                out.append(t)
            elif t in prec:
                while stack and stack[-1] in prec and prec[stack[-1]] >= prec[t]:
                    out.append(stack.pop())
                stack.append(t)
            elif t == "(":
                stack.append(t)
            elif t == ")":
                while stack and stack[-1] != "(":
                    out.append(stack.pop())
                stack.pop()
        while stack:
            out.append(stack.pop())
        return out

    def parse(self, expr: str) -> TreeNode:
        tokens = self.tokenize(expr)
        rpn = self.to_rpn(tokens)
        stack: List[TreeNode] = []
        for t in rpn:
            if t.isdigit() or self._is_float(t):
                stack.append(TreeNode(float(t)))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(TreeNode(t, left, right))
        return stack[0]

    def _is_float(self, s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False
