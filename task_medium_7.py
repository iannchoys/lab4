from collections.abc import Callable
from functools import wraps
from typing import Any


def log_call(function: Callable[..., Any]) -> Callable[..., Any]:
    """Логировать вызов декорированной функции."""

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Вызов функции: {function.__name__}")
        return function(*args, **kwargs)

    return wrapper


@log_call
def greet(name: str) -> str:
    """Вернуть приветствие."""
    return f"Привет, {name}!"


if __name__ == "__main__":
    print(greet("Анна"))
