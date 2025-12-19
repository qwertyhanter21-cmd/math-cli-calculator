import logging
import json
from datetime import datetime
from pathlib import Path

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        entry = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": record.levelname,
            "module": record.module,
            "func": record.funcName,
            "message": record.getMessage(),
        }
        if record.exc_info:
            entry["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(entry, ensure_ascii=False)

def get_logger(name: str = "math-cli", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # щоб не дублювати хендлери

    logger.setLevel(level)

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    fh = logging.FileHandler(log_dir / "app.log", encoding="utf-8")
    fh.setFormatter(JsonFormatter())
    fh.setLevel(level)

    ch = logging.StreamHandler()
    ch.setFormatter(JsonFormatter())
    ch.setLevel(level)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
