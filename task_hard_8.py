import csv
from pathlib import Path


def is_it_employee(employee: dict[str, str]) -> bool:
    """Проверить, работает ли сотрудник в отделе IT."""
    return employee["department"] == "IT"


def transform_employee(employee: dict[str, str]) -> dict[str, str]:
    """Преобразовать данные сотрудника."""
    increased_salary = float(employee["salary"]) * 1.10

    return {
        "name": employee["name"].upper(),
        "age": employee["age"],
        "department": employee["department"],
        "salary": f"{increased_salary:.2f}",
    }


def process_csv(
    input_path: Path,
    output_path: Path,
) -> list[dict[str, str]]:
    """Отфильтровать и преобразовать данные CSV через filter и map."""
    with input_path.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as input_file:
        employees = list(csv.DictReader(input_file))

    filtered_employees = filter(is_it_employee, employees)
    transformed_employees = list(
        map(transform_employee, filtered_employees)
    )

    fieldnames = ["name", "age", "department", "salary"]

    with output_path.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transformed_employees)

    return transformed_employees


if __name__ == "__main__":
    source_file = Path(__file__).with_name("employees.csv")
    result_file = Path(__file__).with_name("filtered_employees.csv")

    result = process_csv(source_file, result_file)

    for employee in result:
        print(employee)
