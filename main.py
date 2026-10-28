from pathlib import Path

from task_hard_6 import show_message
from task_hard_8 import process_csv
from task_medium_1 import get_squares
from task_medium_5 import fibonacci
from task_medium_7 import greet


def main() -> None:
    """Продемонстрировать выполнение лабораторной работы №4."""
    print("Среднее задание №1 — квадраты через map")
    print(get_squares())

    print("\nСреднее задание №5 — генератор Фибоначчи")
    print(list(fibonacci(10)))

    print("\nСреднее задание №7 — декоратор логирования")
    print(greet("Анна"))

    print("\nПовышенное задание №6 — декоратор с параметрами")
    show_message("Функция вызвана")

    print("\nПовышенное задание №8 — CSV через map/filter")
    source_file = Path(__file__).with_name("employees.csv")
    result_file = Path(__file__).with_name("filtered_employees.csv")

    employees = process_csv(source_file, result_file)

    for employee in employees:
        print(employee)


if __name__ == "__main__":
    main()
