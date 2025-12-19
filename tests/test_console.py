import subprocess
import sys
from pathlib import Path


def run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-m", "src.console", *args],
                          capture_output=True, text=True)


def test_run_and_list(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    Path("data").mkdir(exist_ok=True)

    r1 = run_cli("run", "(2+3)*4")
    assert " = 20.0" in r1.stdout

    r2 = run_cli("list")
    assert "(2+3)*4 = 20.0" in r2.stdout
