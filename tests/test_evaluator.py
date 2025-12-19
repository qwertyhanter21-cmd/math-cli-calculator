from src.parser import ExpressionParser
from src.evaluator import Evaluator


def test_eval_basic():
    tree = ExpressionParser().parse("2+3*4")
    result = Evaluator().eval(tree)
    assert result == 14.0


def test_division_by_zero():
    tree = ExpressionParser().parse("10/0")
    try:
        Evaluator().eval(tree)
        assert False, "Мало бути виключення ZeroDivisionError"
    except ZeroDivisionError:
        assert True
