from typing import Literal


def say_hello() -> Literal["Hello from pyproject-test!"]:
    return "Hello from pyproject-test!"


def say_personalized_hello(name: str) -> str:
    return f"Hello {name}"
