from collections.abc import Iterator


def fibonacci(count: int) -> Iterator[int]:
    """Сгенерировать count чисел последовательности Фибоначчи."""
    if count < 0:
        raise ValueError("Количество чисел не может быть отрицательным.")

    first = 0
    second = 1

    for _ in range(count):
        yield first
        first, second = second, first + second


if __name__ == "__main__":
    print(list(fibonacci(10)))
