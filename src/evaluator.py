from .expression_tree import TreeNode


class Evaluator:
    """Обхід дерева та обчислення значення виразу."""

    def eval(self, node: TreeNode) -> float:
        if node.is_leaf():
            # Лист обов'язково має містити число (float), не оператор
            return float(node.value)

        op = node.value
        left = self.eval(node.left) if node.left else 0.0
        right = self.eval(node.right) if node.right else 0.0

        if op == "+":
            return left + right
        if op == "-":
            return left - right
        if op == "*":
            return left * right
        if op == "/":
            if right == 0:
                raise ZeroDivisionError("Ділення на нуль")
            return left / right

        raise ValueError(f"Невідомий оператор: {op}")
