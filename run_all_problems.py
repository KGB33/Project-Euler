#!/usr/bin/env python3
import importlib
import inspect
import pkgutil
from typing import Iterator, NoReturn, Callable
import re

from pathlib import Path
from colorama import init, deinit, Style, Fore

import problems

PROBLEM_NAME_REGEX = re.compile(r"problems.p\d\d\d")


def walk_problems() -> Iterator[str]:
    def on_error(name: str) -> NoReturn:
        raise ImportError(name=name)

    for module in pkgutil.walk_packages(
        problems.__path__, f"{problems.__name__}.", onerror=on_error
    ):
        if not PROBLEM_NAME_REGEX.match(module.name):
            continue
        try:
            imported = importlib.import_module(module.name)
        except:
            pass  # catch errors in test_problem so they're pretty printed
        if not inspect.isfunction(getattr(imported, "test_solution", None)):
            continue
        yield module.name


def test_problem(module):
    test_solution = get_test_func(module)
    try:
        pass_, time = test_solution()
        if pass_:
            print(
                f"{Fore.GREEN}{module}{Style.RESET_ALL} in {color_code_time(time)}{Style.RESET_ALL}"
            )
        else:
            print(
                f"{Fore.RED}{module}{Style.RESET_ALL} in {color_code_time(time)}{Style.RESET_ALL}"
            )
    except Exception as e:
        print(f"{Fore.RED}{module} -- {e}{Style.RESET_ALL}")


def get_test_func(module) -> Callable:
    spec = importlib.util.find_spec(module)
    lib = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lib)
    return getattr(lib, "test_solution")


def color_code_time(time: int) -> str:
    """
    TODO: Use python 3.10 Match case to make this pretty colors
    """
    return f"{Style.RESET_ALL}{time}"


if __name__ == "__main__":
    init()
    for problem in walk_problems():
        test_problem(problem)
    deinit()
