import json
from pathlib import Path
from typing import List, Dict


class Storage:
    """Проста історія виразів у файлі data/history.json."""

    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

    def list(self) -> List[Dict]:
        return json.loads(self.path.read_text(encoding="utf-8"))

    def create(self, expression: str, result: float) -> None:
        data = self.list()
        data.append({"expression": expression, "result": result})
        self.path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def delete(self, index: int) -> bool:
        data = self.list()
        if 0 <= index < len(data):
            data.pop(index)
            self.path.write_text(
                json.dumps(data, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            return True
        return False
