import argparse
from pathlib import Path
from .parser import ExpressionParser
from .evaluator import Evaluator
from .storage import Storage


def build_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="math-cli",
        description=(
            "Консольний інтерпретатор математичних виразів " "(+ - * /, дужки)."
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Обчислити вираз")
    run.add_argument(
        "expression",
        type=str,
        help="Напр.: (2+3)*4",
    )

    sub.add_parser("list", help="Показати історію обчислень")

    delp = sub.add_parser("delete", help="Видалити запис з історії за індексом")
    delp.add_argument(
        "index",
        type=int,
        help="Індекс запису (0..n)",
    )

    return parser


def main():
    args = build_cli().parse_args()
    storage = Storage(Path("data/history.json"))
    parser = ExpressionParser()
    evaluator = Evaluator()

    if args.command == "run":
        tree = parser.parse(args.expression)
        result = evaluator.eval(tree)
        storage.create(args.expression, result)
        print(f"{args.expression} = {result}")

    elif args.command == "list":
        data = storage.list()
        if not data:
            print("Історія порожня.")
        else:
            for i, item in enumerate(data):
                print(f"[{i}] {item['expression']} = {item['result']}")

    elif args.command == "delete":
        ok = storage.delete(args.index)
        print("Видалено." if ok else "Помилка: індекс поза межами.")


if __name__ == "__main__":
    main()
