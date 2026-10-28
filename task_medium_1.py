def get_squares() -> list[int]:
    """Вернуть квадраты чисел от 1 до 10 с помощью map."""
    numbers = range(1, 11)
    return list(map(lambda number: number ** 2, numbers))


if __name__ == "__main__":
    print(get_squares())
