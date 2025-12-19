from src.parser import ExpressionParser


def test_tokenize_simple():
    p = ExpressionParser()
    assert p.tokenize("2+3") == ["2", "+", "3"]


def test_rpn_parentheses():
    p = ExpressionParser()
    rpn = p.to_rpn(p.tokenize("(2+3)*4"))
    assert rpn == ["2", "3", "+", "4", "*"]


def test_build_tree_structure():
    p = ExpressionParser()
    tree = p.parse("2*(3+4)")
    assert tree.value == "*"
    assert tree.left.value == 2.0
    assert tree.right.value == "+"
    assert tree.right.left.value == 3.0
    assert tree.right.right.value == 4.0
