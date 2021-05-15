#!/usr/bin/env python3

import os
from pathlib import Path
from colorama import init, deinit, Style

if __name__ == "__main__":
    init()
    path = Path(__file__).parent.absolute() / "problems"
    problems = sorted([f for f in path.iterdir() if f.is_file()])

    for problem in problems:
        if "016" in problem.name:
            break
        print(Style.RESET_ALL)
        print(f"\n\n---------- Problem {problem.name} ----------")
        os.system(f"python {problem}")
    deinit()
