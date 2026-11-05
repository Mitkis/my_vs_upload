import subprocess
import sys
from pathlib import Path


class calculator:
    def add(self, a,b):
        return a+b
    def substract(self, a,b):
        return a-b
    def multiply(self, a,b):
        return a*b
    def divide(self, a,b):
        if b==0:
            return("Cannot divide by zero")
        else:
            return a/b

calc = calculator()

if __name__ == "__main__":
    app_path = (
        Path.home()
        / "Desktop"
        / "AutoCAD_2016_English_Win_64bit"
        / "calculator_app.py"
    )
    if not app_path.is_file():
        raise FileNotFoundError(f"Calculator app not found: {app_path}")
    subprocess.Popen(
        [sys.executable, str(app_path)],
        cwd=app_path.parent,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
