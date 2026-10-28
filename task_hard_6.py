from collections.abc import Callable
from functools import wraps
from typing import Any


def repeat(
    times: int,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Создать декоратор, повторяющий вызов функции times раз."""
    if times <= 0:
        raise ValueError("Количество повторений должно быть положительным.")

    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result: Any = None

            for _ in range(times):
                result = function(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3)
def show_message(message: str) -> None:
    """Вывести сообщение."""
    print(message)


if __name__ == "__main__":
    show_message("Функция вызвана")
