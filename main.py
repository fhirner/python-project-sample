from typing import Any

from rich import print

from greeters.hello import say_hello


def returner(foo: Any) -> dict[str, int | bool | Any]:
    return {"a": 1, "b": True, "foo": foo}


def main() -> None:
    print(f"[italic red]{say_hello()}[/italic red]")


if __name__ == "__main__":
    main()
