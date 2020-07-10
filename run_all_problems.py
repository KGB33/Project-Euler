#!/usr/bin/env python3

import os
from pathlib import Path

if __name__ == "__main__":
    path = Path(__file__).parent.absolute() / "problems"
    problems = sorted([f for f in path.iterdir() if f.is_file()])

    for problem in problems:
        print(f"\n\n---------- Problem {problem.name} ----------")
        os.system(f"python {problem}")
